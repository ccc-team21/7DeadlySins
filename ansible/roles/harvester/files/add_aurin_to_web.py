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
# this script adds the aurin data to the database

import requests
import json
import couchdb
import sys
USERNAME = 'admin'
PASSWORD = 'admin'
DATABASEADDRESS=sys.argv[1] #a.b.c.d:port
DATABASENAME = 'aurin_richness'
#scale for the aurin data
mult_fact = 10
#VIEWINDEX = 'words_twe'

# this method adds document to the CouchDB.

def write_couchdb(id, d):

    databaseURL = "http://%s:5984/%s"%(DATABASEADDRESS,DATABASENAME)
    headerss = {"Content-Type": "application/json"}
    response = requests.put(databaseURL + '/' + str(id), data=json.dumps(d), headers=headerss)
    print(response)
    print(response.content)
    print("\n\n\n\n\n")


#this file has the polygon coordinates of each suburb
with open('melb_geojson.json') as f:
    js_melb = json.load(f)

#this file has the aurin data to be used for analysis
with open('aurin.json') as f:
    js_aurin = json.load(f)


suburb_dic = {}
for feature in js_melb['features']:
    suburb_dic[feature['properties']['cartodb_id']] = {}
    suburb_dic[feature['properties']['cartodb_id']]['name'] = feature['properties']['name'].lower()
    suburb_dic[feature['properties']['cartodb_id']]['aurin'] = ""
    



#saving aurin data to a dictionary to be used later
aurin_dic = {}
for feature in js_aurin['features']:
	aurin_dic[feature['properties']['SSC_NAME']] = {}
	aurin_dic[feature['properties']['SSC_NAME']]['id'] = feature['properties']['SSC2011']
	aurin_dic[feature['properties']['SSC_NAME']]['uni'] = feature['properties']['uni']
	aurin_dic[feature['properties']['SSC_NAME']]['emp_to_pop'] = feature['properties']['emp_to_pop']
	aurin_dic[feature['properties']['SSC_NAME']]['median11'] = feature['properties']['median11']

count = 0

melbourne_ids = []


min_rich = float(10000000000000000)
max_rich = float(-1000000000000000)
#for each suburb id, add get corresponding aurin name by comparing the name of suburb with aurin's suburb names
for item in suburb_dic:
	for aurin_item in aurin_dic:
		if suburb_dic[item]['name'] == 'melbourne (3004)' or suburb_dic[item]['name'] == 'melbourne (3000)':
			melbourne_ids.append(item)
			suburb_dic[item]['aurin'] = 'Melbourne'
			suburb_dic[item]['uni'] = aurin_dic['Melbourne']['uni']
			suburb_dic[item]['emp_to_pop'] = aurin_dic['Melbourne']['emp_to_pop']
			suburb_dic[item]['median11'] = aurin_dic['Melbourne']['median11']
			suburb_dic[item]['richness'] = suburb_dic[item]['emp_to_pop'] * suburb_dic[item]['median11']
			break
		if suburb_dic[item]['name'] == aurin_item.replace('(Vic.)','').lower().strip():
			#adding aurin details  to suburb dic
			suburb_dic[item]['aurin'] = aurin_item
			suburb_dic[item]['uni'] = aurin_dic[aurin_item]['uni']
			suburb_dic[item]['emp_to_pop'] = aurin_dic[aurin_item]['emp_to_pop']
			suburb_dic[item]['median11'] = aurin_dic[aurin_item]['median11']
			#calculating richness
			suburb_dic[item]['richness'] = suburb_dic[item]['emp_to_pop'] * suburb_dic[item]['median11'] 
			#calculating min and max to be used for scaling the data
			if min_rich>float(suburb_dic[item]['richness']):
				min_rich= suburb_dic[item]['richness']
			if max_rich<float(suburb_dic[item]['richness']):
				max_rich= suburb_dic[item]['richness']
			count+=1
			break

#add each item to db after scaling the score
for item in suburb_dic:
	name = suburb_dic[item]['name']
	aurin_name = suburb_dic[item]['aurin']
	current_richness = suburb_dic[item]['richness']
	#score is scaled to mult factor
	score = ((current_richness-min_rich)/(max_rich-min_rich))*mult_fact
	d = {}

	d['name'] = name
	d['aurin_name'] = aurin_name
	d['score'] = score
	write_couchdb(item, d)

