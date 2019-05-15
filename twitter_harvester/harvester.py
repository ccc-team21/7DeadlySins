'''
Team 21 Deadly Sin Analysis
City: Melbourne
Team Members:
    Anupa Alex : 1016435
    Luiz Fernando Franco : 1019613
    Suraj Kumar Thakur : 999886
    Waneya Iqbal : 919750
    Yan Li : 984120
'''

#This script uses Twitter's streaming API for harvesting data from twitter based on location

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import time
import json
from shapely.geometry import shape, Point, Polygon
import requests
import numpy as np

from wordsegment import segment,load
import json
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import SnowballStemmer
from nltk.corpus import stopwords
import unicodedata
lmt = WordNetLemmatizer()

#Removd keys
TWITTER_API_KEY=''
TWITTER_API_SECRET=''
TWITTER_ACCESS_KEY=''
TWITTER_ACCESS_SECRET=''

#authenticating with twitter
auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_ACCESS_KEY,TWITTER_ACCESS_SECRET)

print("Start time of script", time.time())
MELB_GEOJSON = '../data/melb_geojson.json'
DB_ADDRESS="variable set by ansible"
#stop words to be used for processing text
stop_words = set(stopwords.words('english'))
# load GeoJSON file containing suburbs
with open(MELB_GEOJSON) as f:
    js = json.load(f)

#saving suburb id and name to a dictionary to be used later
suburb_dic = {}
suburb_name_dic = {}
for feature in js['features']:
    suburb_dic[feature['properties']['cartodb_id']]= feature['properties']['name']
    suburb_name_dic[feature['properties']['name'].lower()]= feature['properties']['cartodb_id']


#this method is used to preprocess the text using NLP before adding to atabase
def process_text(text):
    normalised_tokens = []
    split_text = unicodedata.normalize('NFKD', text).encode("utf-8").lower().split()
    
    for token in split_text:
        word = token.lower()
        #excluding stop words
        if word not in stop_words:
            #using lemmatization
            normalised = lmt.lemmatize(word)
            normalised_tokens.append(normalised)
            #segmenting tokens and adding to database
            segmented_tokens = segment(word)
            if len(segmented_tokens) > 1:
                for item in segmented_tokens:
                    if item not in stop_words:
                        normalised_tokens.append(lmt.lemmatize(item))
    
    print(' '.join(normalised_tokens))
    return ' '.join(normalised_tokens)


# this method returns the suburb id from the coordinate by checking if the point lies in the polygon
def get_suburb_frm_point(coord):
    suburb_id = -1
    for feature in js['features']:
        poly_coord = np.array(feature['geometry']['coordinates'][0][0])
        poly_tup = [tuple(l) for l in poly_coord]
        polygon = Polygon(poly_tup)
        if coord.within(polygon):
            suburb_id = feature['properties']['cartodb_id']
            break
        
    return suburb_id


# this method returns the suburb id from the coordinate by checking if the polygon in place field overlaps with the polygon of suburb
#the suburb with maxiimum overlap is chosen
def get_suburb_frm_place(place):
    places = place['bounding_box']['coordinates']
    max_area = 0 
    max_area_sub_id = -1
    for place in places:
        place_polygon = Polygon(place)
        for feature in js['features']:
            suburb_polygon = shape(feature['geometry'])
            if place_polygon.intersects(suburb_polygon):
                area = place_polygon.intersection(suburb_polygon).area
                if area>max_area:
                    max_area = area
                    max_area_sub_id = feature['properties']['cartodb_id']
                    

    return max_area_sub_id
            

#this method calculates suburb id based on the user location by matching the names of suurb with user location
def get_suburb_id_frm_user_loc(user_loc):
    split_coma = user_loc.split(',')
    for item in split_coma:
        if item.lower().strip() in suburb_name_dic:
            return suburb_name_dic[item.lower().strip()]
    split_space = user_loc.split(' ')
    for item in split_space:
        if item.lower().strip() in suburb_name_dic:
            return suburb_name_dic[item.lower().strip()]       
    return -1

#this method get suburb id from either of the three methods: coordinatesor place or user location
def get_suburb_id(coord,user_loc):
    suburb_id = -1
    from_coord = False
    according = None
    if coord!=None:
        coord_list = coord['coordinates']
        point = Point(coord_list[0],coord_list[1])
        suburb_id = get_suburb_frm_point(point)
        from_coord = True
        according = "coordinates"
    elif user_loc!=None and suburb_id==-1:
        suburb_id = get_suburb_id_frm_user_loc(user_loc)
        according = "user_loc"
    return suburb_id,from_coord,according



     
#this method processes the tweet and stores only the fileds required for analysis
def process_tweet(tweet):  
    #print(tweet)
    d = {}
    id_db = tweet['id']
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = process_text(tweet['text'])
    d['coordinates'] = tweet['coordinates']
    #d['place'] = tweet['place']
    d['user_loc'] = tweet['user']['location']
    d['source'] = 'stream'
    suburb_id,from_coord,according = get_suburb_id(tweet['coordinates'],tweet['user']['location'])
    if suburb_id!=-1:
        d['suburb_id'] = suburb_id
        d['from_coord'] = from_coord
        d['according'] =  according
        return id_db,d
    else:
        return None,None


# this method adds file to the CouchDB.
# Look at the use of http command PUT
# and the use of tweet id. This filters
# out duplicate tweets.
def write_couchdb(id, d):
    databaseURL = "http://%s:5984/twitter_streaming"%(DB_NAME)
    headerss = {"Content-Type": "application/json"}
    response = requests.put(databaseURL + '/' + str(id), data=json.dumps(d), headers=headerss)

#initialising back off values according to twitter API    
network_error_backoff = 0.25
http_error_backoff = 5
rate_limit_backoff = 60
class MyListener(StreamListener):

    def on_data(self, raw_data):
        try:

            tweet = json.loads(raw_data)
            if tweet['coordinates'] !=None or tweet['place']!=None or tweet['user']['location']!=None:
                id_db,processed_tweet = process_tweet(tweet)
                if processed_tweet!=None:
                   
                    write_couchdb(id_db, processed_tweet)

                
            else:
                print("All none")
                return True
        except BaseException as e:
            print(raw_data)
            print("Error on_data:%s" % str(e))
        return True
        
    def on_error(self, status_code):
        global rate_limit_backoff
        global http_error_backoff
        if status_code == 420:
            print("ERROR: Rate limit reached")
            time.sleep(rate_limit_backoff)
            #exponential backoff
            rate_limit_backoff *= 2
        else:
            time.sleep(http_error_backoff)
            #expenential backoff for http error
            http_error_backoff = min(2*http_error_backoff,320)
        print(status_code)
        return True

    def on_timeout(self):
        global network_error_backoff
        print("ERROR: Timeout...")
        #linear back off for network error
        time.sleep(network_error_backoff)
        return True  # Don't kill the stream
        
twitter_stream = Stream(auth, MyListener())

# use filter to collect twitter information based on Australia field
while True:
    try:
        print("Connection.............................................")
        #resetting values for new connection
        http_error_backoff = 5
        rate_limit_backoff = 60
        twitter_stream.filter(locations=[145.12,-38.45,145.53,-37.38])
    except Exception as e:
        print(e)
        #linear backoff for network errors
        time.sleep(network_error_backoff)
        network_error_backoff = min(network_error_backoff + 0.25, 16)
    pass
