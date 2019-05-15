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
#This script reads the data from a file which has Instagram data from the couchDB given in the Appendix of Project SPecification
#Image is downloaded for each document and processed to find if it is adult content and also to count number of faces in each image.
#After processing this data is added to the instagram_data database in Couch DB


import os
import cv2
import sys
import urllib
from bs4 import BeautifulSoup
import nude
from nude import Nude
from shapely.geometry import shape, Point, Polygon
import requests
import numpy as np
import json
import sys


year = sys.argv[1]
n = sys.argv[2]
DB_SERVER = "172.26.38.106"
#file where instagram data is saved
f_name = '../data/instagram_%s_%s.json'%(year,n)
len_file = os.path.getsize(f_name)
fp = open(f_name)
count = 0



#this file has the polygon coordinates of each suburb
with open('../data/melb_geojson.json') as f:
    js = json.load(f)

#saving suburb id and name to a dictionary to be used later
suburb_dic = {}
suburb_name_dic = {}
for feature in js['features']:
    suburb_dic[feature['properties']['cartodb_id']]= feature['properties']['name']
    suburb_name_dic[feature['properties']['name'].lower()]= feature['properties']['cartodb_id']

#this method is used to write data to the database after processing
def write_couchdb(id, d):

    # Cluster 1  VM IP
    databaseURL = "http://%s:5984/instagram_data"%(DB_SERVER)
    headerss = {"Content-Type": "application/json"}
    response = requests.put(databaseURL + '/' + str(id), data=json.dumps(d), headers=headerss)
    print(response)
    print(response.content)
    print("\n\n\n\n\n")

#this method is used to download image from a given url
def get_image_from_url(url):
	global year
	f = urllib.urlopen(url)
	htmlSource = f.read()
	soup = BeautifulSoup(htmlSource,'html.parser')
	#print(soup)
	metaTag = soup.find_all('meta', {'property':'og:image'})
	#print(metaTag)
	imgURL = metaTag[0]['content']
	image_path = "./images/instagram_%s_img_%d.jpg"%(year,count)
	urllib.urlretrieve(imgURL, image_path)
	print 'Done. Image saved to disk as ' + image_path
	
	return image_path


#this method uses OPenCV and cascades to detect faces in image
def get_face_count(image_path):
	casc_path = "haarcascade_frontalface_default.xml"
	face_cascade = cv2.CascadeClassifier(casc_path)
	image = cv2.imread(image_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30, 30),
	flags = cv2.CASCADE_SCALE_IMAGE
	)
	return len(faces)

#this method uses nudepy library to check if an image is adult content
def get_nude(image_path):
	return nude.is_nude(image_path)


# this method returns the suburb id from the coordinate by checking if the point lies in the polygon
def get_suburb_frm_point(coord):
    #print(coord)
    suburb_id = -1
    for feature in js['features']:
        poly_coord = np.array(feature['geometry']['coordinates'][0][0])
        poly_tup = [tuple(l) for l in poly_coord]
        polygon = Polygon(poly_tup)
        if coord.within(polygon):
            suburb_id = feature['properties']['cartodb_id']
            print(suburb_id)
            break
        
    return suburb_id

#iterate through each line in the instgram data,
while fp.tell()<len_file:
	
		row= fp.readline().strip()
		count+=1
		try:
			#for every row, the last character is ',' hence ignoring the last character
			row = json.loads(row[0:len(row)-1])				
		except Exception as e:
			try:
				#for the last but one row, there is no ',' at the end as it is the last element of the JSON array
				row = json.loads(row[0:len(row)])
			except Exception as e:
				print(e)
				#there will be exception for the last line which is not a valid JSON
				continue
		try:
			print(row["doc"]["coordinates"]["coordinates"])
			if "coordinates" in row["doc"] and row["doc"]["coordinates"]!=None:
				coordinates = row["doc"]["coordinates"]["coordinates"]
				coord = Point(coordinates[1],coordinates[0])
				suburb_id = get_suburb_frm_point(coord)
				#only if the suburb id is not -1, we try to process the image
				if suburb_id!=-1:
					url = row["doc"]["link"]
					insta_id = row["doc"]["id"]
					#download image and get downloaded path
					image_path = get_image_from_url(url)
					#get nuber of faces in the image
					face_count = get_face_count(image_path)
					is_nude = get_nude(image_path)
					#creating a dictionary to be added to the database
					insta_dic = {}
					insta_dic["face_count"]=face_count
					insta_dic["is_nude"]=is_nude
					insta_dic["suburb_id"] = suburb_id
					insta_dic["coordinates"] = coordinates
					insta_dic["year"] = year
					write_couchdb(insta_id,insta_dic)
					count+=1						
			
		except Exception as e:
			print(e)
			continue