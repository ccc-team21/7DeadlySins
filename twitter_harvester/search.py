'''
Team 21 Deadly Sin Analysis
City: Melbourne
Team Members:
    Anupa Alex – 1016435
    Luiz Fernando Franco - 1019613
    Suraj Kumar Thakur - 999886
    Waneya Iqbal - 919750
    Yan Li – 984120
'''
#this script uses Twitter's search API to get data upto 7 days back.
# It uses location filter to get data from in and around Melbourne.

import json
import sys
# from geojson_utils import centroid
import time

import numpy as np
import requests
import tweepy
from shapely.geometry import shape, Point,Polygon
from wordsegment import segment,load
import requests
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import SnowballStemmer
from nltk.corpus import stopwords
import unicodedata

print("Start time of script", time.time())
#this file has the polygon coordinates of each suburb
MELB_GEOJSON = '../data/melb_geojson.json'
DB_ADDRESS="172.26.38.10"
#stop words to be used for processing text
stop_words = set(stopwords.words('english'))
#Removd keys
TWITTER_API_KEY='8r5I2kHD90M9LrjYLyzCpT5Ub'
TWITTER_API_SECRET='qCi4zLj8whxYbN6ixWgbl22Xgw4DPhyf9ldVnfcYvlSpYpguMX'
TWITTER_ACCESS_KEY='100484448-DT1U7MBwNdMLvYV9WUo8mnZFnvi7c2WKg74hW995' 
TWITTER_ACCESS_SECRET='wgpsBFYZreHny91RjlE74I9nGMT35EgYqDqIwTt941tda'

#authenticating with twitter
auth = tweepy.AppAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

if (not api):
    print("Can't Authenticate")
    sys.exit(-1)

# load GeoJSON file containing sectors

with open(MELB_GEOJSON) as f:
    js = json.load(f)
#saving suburb id and name to a dictionary to be used later
suburb_dic = {}
suburb_name_dic = {}
for feature in js['features']:
    suburb_dic[feature['properties']['cartodb_id']] = feature['properties']['name'].lower()
    suburb_name_dic[feature['properties']['name'].lower()] = feature['properties']['cartodb_id']
suburb_name_dic['melbourne'] = 122


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
    #all the tokens are joind to make text
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
                if area > max_area:
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

#get suburb id from either of the three methods: coordinatesor place or user location
def get_suburb_id(coord, user_loc):
    suburb_id = -1
    from_coord = False
    according = None
    if coord != None:
        coord_list = coord['coordinates']
        point = Point(coord_list[0], coord_list[1])
        suburb_id = get_suburb_frm_point(point)
        from_coord = True
        according = "coordinates"
    elif user_loc != None and suburb_id == -1:
        suburb_id = get_suburb_id_frm_user_loc(user_loc)
        according = "user_loc"
    return suburb_id, from_coord, according

#this method processes the tweet and stores only the fileds required for analysis
def process_tweet(tweet):
    # print(tweet)
    try:
        d = {}
        id_db = tweet['id']
        d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
        d['text'] = process_text(tweet['text'])
        d['coordinates'] = tweet['coordinates']
        d['user_loc'] = tweet['user']['location']
        d['source'] = 'location_search'
        suburb_id, from_coord, according = get_suburb_id(tweet['coordinates'], tweet['user']['location'])
        if suburb_id != -1:
            d['suburb_id'] = suburb_id
            d['from_coord'] = from_coord
            d['according'] = according
            return id_db, d
        else:
            return None, None
    except Exception as e:
        return None, None



# this method adds file to the CouchDB.
# Look at the use of http command PUT
# and the use of tweet id. This filters
# out duplicate tweets.
def write_couchdb(id, d):
    databaseURL = "http://%s:5984/twitter_streaming"%(DB_NAME)
    headerss = {"Content-Type": "application/json"}
    response = requests.put(databaseURL + '/' + str(id), data=json.dumps(d), headers=headerss)
    
    

def search(geocode):
    # print(geocode)

    searchQuery = '*'  #when search with geocode
    tweetsPerQry = 100  # this is the max the API permits

    sinceId = None
    max_id = -1
    count = 0
    tweetCount = 0
    while True:

        try:
            #request for 100 tweets
            new_tweets = api.search(q=searchQuery, count=tweetsPerQry, geocode=geocode)
            if not new_tweets:
                print("No more tweets found")
                break
            count = 0
            #process each tweet
            for tweet in new_tweets:
                tweet_json = tweet._json
                id_db, processed = process_tweet(tweet_json)
                if processed != None:
                    #write_couchdb(id_db, processed)
                    count += 1

            
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break
#centre of melbourne with radius 300 km
geocode = "%f,%f,%fkm" % (-37.817457, 145.002606, 300)
search(geocode)