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
# This script keeps checking for changes in view and
# updates the web server databases when there is any change in the views
#Takes IP of Database Server as Input as 
import json
import requests
import couchdb
import time
import sys

#seclaring variables used
twitter_total_count_dic = {}
twitter_lust_count_dic = {}
twitter_pride_count_dic = {}
twitter_lust_divided_dic = {}
twitter_pride_divided_dic = {}

insta_total_count_dic = {}
insta_lust_count_dic = {}
insta_pride_count_dic = {}
insta_lust_divided_dic = {}
insta_pride_divided_dic = {}

lust_web_db = 'lust_web'
pride_web_db = 'pride_web'

total_count_view = 'count'
lust_count_view = 'count-lust'
pride_count_view = 'count-pride'

USERNAME = 'admin'
PASSWORD = 'admin'
DATABASEADDRESS=sys.argv[1]
TWITTER_DATABASENAME = 'twitter_streaming'
INSTA_DATABASENAME = 'instagram_data'
TWITTER_DESIGNNAME = 'Twitter_Analysis'
INSTA_DESIGNNAME = 'Insta_Analysis'
sleep_time = 600
mult_factor = 10
pride_min = 10000000000000000000000
lust_min = 10000000000000000000000
pride_max = -10000000000000000000000
lust_max = -10000000000000000000000


#this file has the polygon coordinates of each suburb
with open('../data/melb_geojson.json') as f:
    js_melb = json.load(f)

#this file has the aurin data to be used for analysis
with open('../data/aurin.json') as f:
    js_aurin = json.load(f)

#saving suburb id and name to a dictionary to be used later
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
for item in suburb_dic:
	for aurin_item in aurin_dic:
		if suburb_dic[item]['name'] == 'melbourne (3004)' or suburb_dic[item]['name'] == 'melbourne (3000)':
			suburb_dic[item]['aurin'] = 'Melbourne'
			suburb_dic[item]['uni'] = aurin_dic['Melbourne']['uni']
			suburb_dic[item]['emp_to_pop'] = aurin_dic['Melbourne']['emp_to_pop']
			suburb_dic[item]['median11'] = aurin_dic['Melbourne']['median11']
			suburb_dic[item]['richness'] = suburb_dic[item]['emp_to_pop'] * suburb_dic[item]['median11']
			break
		if suburb_dic[item]['name'] in aurin_item.lower().replace('(Vic.)','').strip():
			suburb_dic[item]['aurin'] = aurin_item
			suburb_dic[item]['uni'] = aurin_dic[aurin_item]['uni']
			suburb_dic[item]['emp_to_pop'] = aurin_dic[aurin_item]['emp_to_pop']
			suburb_dic[item]['median11'] = aurin_dic[aurin_item]['median11']
			suburb_dic[item]['richness'] = suburb_dic[item]['emp_to_pop'] * suburb_dic[item]['median11']
			count+=1
			break


#this method returns the content of the input view as a dictionary
def get_view_as_dic(view_name,db_name,design_name,group_level):
	databaseURL = "http://%s:%s@%s:5984/%s/_design/%s/_view/%s" % (USERNAME, PASSWORD,DATABASEADDRESS,db_name,design_name,view_name)
	headerss = {"Content-Type": "application/json"}
	parameters= {'reduce': 'true', 'group_level':group_level}
	count =0
	dic = {}
	with requests.get(databaseURL , params=parameters, stream = True) as response:
		for row in response.iter_lines():
			try:
				#for every row, the last character is ',' hence ignoring the last character
				row = json.loads(row[0:len(row)-1])	
				dic[row['key']] = row['value']
				count+=1		
			except Exception as e:
				try:
					#for the last but one row, there is no ',' at the end as it is the last element of the JSON array
					row = json.loads(row[0:len(row)])
					dic[row['key']] = row['value']
					count +=1
				except Exception as e:
					#there will be exception for the last line which is not a valid JSON
					print("oops")
					
	return dic


#Getting Twitter views after map reduce........................
#get total
twitter_total_count_dic = get_view_as_dic(total_count_view,TWITTER_DATABASENAME,TWITTER_DESIGNNAME,2)
#get lust
twitter_lust_count_dic = get_view_as_dic(lust_count_view,TWITTER_DATABASENAME,TWITTER_DESIGNNAME,2)
#get pride
twitter_pride_count_dic = get_view_as_dic(pride_count_view,TWITTER_DATABASENAME,TWITTER_DESIGNNAME,2)

# Getting Instagram views after mapreduce
insta_total_count_dic = get_view_as_dic(total_count_view,INSTA_DATABASENAME,INSTA_DESIGNNAME,2)
#get lust
insta_lust_count_dic = get_view_as_dic(lust_count_view,INSTA_DATABASENAME,INSTA_DESIGNNAME,2)
#get pride
insta_pride_count_dic = get_view_as_dic(pride_count_view,INSTA_DATABASENAME,INSTA_DESIGNNAME,2)

#Some values are not added as they are 0, adding them
for i in range(1,123):
	if i not in twitter_lust_count_dic:
		twitter_lust_count_dic[i] = 0
	if i not in twitter_pride_count_dic:
		print(i)
		twitter_pride_count_dic[i] = 0
	if i not in insta_lust_count_dic:
		print(i)
		insta_lust_count_dic[i] = 0
	if i not in insta_pride_count_dic:
		print(i)
		insta_pride_count_dic[i] = 0


final_lust_dic = {}
final_pride_dic = {}


#Find min and max for lust and pride values to be used for scaling
#also finding the combined value for lust and pride 
for item in twitter_lust_count_dic:
	total_lust = float(twitter_lust_count_dic[item]+insta_lust_count_dic[item])/(twitter_total_count_dic[item]+insta_total_count_dic[item])
	final_lust_dic[item] = total_lust
	if total_lust<lust_min:
		lust_min = total_lust
	if total_lust>lust_max:
		lust_max = total_lust
	total_pride = float(twitter_pride_count_dic[item]+insta_pride_count_dic[item])/(twitter_total_count_dic[item]+insta_total_count_dic[item])
	final_pride_dic[item] = total_pride
	if total_pride<pride_min:
		pride_min = total_pride
	if total_pride>pride_max:
		pride_max = total_pride


#Calculate final value after scaling
for item in twitter_lust_divided_dic:
	current_lust = final_lust_dic[item]
	final_lust_dic[item] = ((current_lust-lust_min)/(lust_max-lust_min))*mult_factor	
	current_pride = final_pride_dic[item]
	final_pride_dic[item] = ((current_pride-pride_min)/(pride_max-pride_min))*mult_factor





#this method adds a document to the DB
def write_couchdb(id, d,db_name):

    databaseURL = "http://%s/%s"%(DATABASEADDRESS,db_name)
    headerss = {"Content-Type": "application/json"}
    response = requests.put(databaseURL + '/' + str(id), data=json.dumps(d), headers=headerss)
    


#adding lust values to web db
for item in final_lust_dic:	
	id_db = item
	d = {}
	d['name'] = suburb_dic[item]['name']
	d['aurin_name'] = suburb_dic[item]['aurin']
	d['score'] = final_lust_dic[item]
	write_couchdb(id_db, d,lust_web_db)


#adding pride value to web db
for item in final_pride_dic:	
	id_db = item
	d = {}
	d['name'] = suburb_dic[item]['name']
	d['aurin_name'] = suburb_dic[item]['aurin']
	d['score'] = final_pride_dic[item]
	write_couchdb(id_db, d,pride_web_db)

#method for updating score in a document
def update_doc_db(db_name,doc_id,score):
	print("Changing score for %s to %f in %s"%(doc_id,score,db_name))
	couch = couchdb.Server("http://%s:%s@%s" % (USERNAME, PASSWORD,DATABASEADDRESS))
	db = couch[db_name]
	doc = db[doc_id]
	doc['score'] = score
	db[doc.id] = doc


#Checking view in a infinite loop evey 10 minutes to make sure that the web db has dynamic data
#if there is any change the web DB will be updated
while True:
	print("Checking View")
	twitter_total_count_dic_dyn = get_view_as_dic(total_count_view,TWITTER_DATABASENAME,TWITTER_DESIGNNAME,2)
	twitter_lust_count_dic_dyn = get_view_as_dic(lust_count_view,TWITTER_DATABASENAME,TWITTER_DESIGNNAME,2)
	twitter_pride_count_dic_dyn = get_view_as_dic(pride_count_view,TWITTER_DATABASENAME,TWITTER_DESIGNNAME,2)

	insta_total_count_dic_dyn = get_view_as_dic(total_count_view,INSTA_DATABASENAME,INSTA_DESIGNNAME,2)
	insta_lust_count_dic_dyn = get_view_as_dic(lust_count_view,INSTA_DATABASENAME,INSTA_DESIGNNAME,2)
	insta_pride_count_dic_dyn = get_view_as_dic(pride_count_view,INSTA_DATABASENAME,INSTA_DESIGNNAME,2)

	for i in range(1,123):
		if i not in twitter_lust_count_dic_dyn:
			print(i)
			twitter_lust_count_dic_dyn[i] = 0
		if i not in twitter_pride_count_dic_dyn:
			print(i)
			twitter_pride_count_dic_dyn[i] = 0
		if i not in insta_lust_count_dic_dyn:
			print(i)
			insta_lust_count_dic_dyn[i] = 0
		if i not in insta_pride_count_dic_dyn:
			print(i)
			insta_pride_count_dic_dyn[i] = 0


	twitter_lust_divided_dic_dyn = {}
	twitter_pride_divided_dic_dyn = {}
	
	insta_lust_divided_dic_dyn = {}
	insta_pride_divided_dic_dyn = {}
	

	for item in twitter_lust_count_dic_dyn:
		twitter_lust_divided_dic_dyn[item] = float(twitter_lust_count_dic_dyn[item])/twitter_total_count_dic_dyn[item]

	for item in twitter_pride_count_dic_dyn:
		twitter_pride_divided_dic_dyn[item] = float(twitter_pride_count_dic_dyn[item])/twitter_total_count_dic_dyn[item]

	for item in insta_lust_count_dic_dyn:
		insta_lust_divided_dic_dyn[item] = float(insta_lust_count_dic_dyn[item])/insta_total_count_dic_dyn[item]

	for item in insta_pride_count_dic_dyn:
		insta_pride_divided_dic_dyn[item] = float(insta_pride_count_dic_dyn[item])/insta_total_count_dic_dyn[item]


	final_lust_dic_dyn = {}
	final_pride_dic_dyn = {}


	for item in twitter_lust_count_dic_dyn:
		total_lust = float(twitter_lust_count_dic[item]+insta_lust_count_dic[item])/(twitter_total_count_dic[item]+insta_total_count_dic[item])
		final_lust_dic_dyn[item] = total_lust
		if total_lust<lust_min:
			lust_min = total_lust
		if total_lust>lust_max:
			lust_max = total_lust


		total_pride = float(twitter_pride_count_dic[item]+insta_pride_count_dic[item])/(twitter_total_count_dic[item]+insta_total_count_dic[item])
		final_pride_dic_dyn[item] = total_pride
		if total_pride<pride_min:
			pride_min = total_pride
		if total_pride>pride_max:
			pride_max = total_pride

	for item in twitter_lust_count_dic_dyn:
		current_lust = final_lust_dic_dyn[item]
		current_pride = final_pride_dic_dyn[item]
		final_lust_dic_dyn[item] = ((current_lust-lust_min)/(lust_max-lust_min))*mult_factor	
		final_pride_dic_dyn[item] = ((current_pride-pride_min)/(pride_max-pride_min))*mult_factor

		if final_lust_dic[item]!=final_lust_dic_dyn[item]:
			update_doc_db(lust_web_db,str(item),final_lust_dic_dyn[item])

		if final_pride_dic[item]!=final_pride_dic_dyn[item]:
			update_doc_db(pride_web_db,str(item),final_pride_dic_dyn[item])


	

	final_lust_dic = final_lust_dic_dyn
	final_pride_dic = final_pride_dic_dyn
	
	print("Sleeping")
	time.sleep(sleep_time)
	
	