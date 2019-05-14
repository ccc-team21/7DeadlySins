'''
Team 21 Sentiment Analysis
City: Melbourne
Team Members:
    Anupa Alex – 1016435
    Luiz Fernando Franco - 1019613
    Suraj Kumar Thakur - 999886
    Waneya Iqbal - 919750
    Yan Li – 984120
'''

from flask import Flask, render_template, jsonify
import json
import couchdb
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


def getdb(database_name):
    couch = couchdb.Server('http://admin:admin@172.26.38.106:5984')
    db = couch[database_name]
    return db


def querydb(database_name):
    db = getdb(database_name)
    lis = []
    newlist = []
    for each in db:
        doc = db[each]
        content = {}
        if doc['name'] == 'mckinnon':
            content['name'] = 'McKinnon'
        else:
            content['name'] = doc['name'].title()
        content['value'] = doc['score']
        lis.append(content)
        newlist = sorted(lis, key=lambda k: k['name'])
    return newlist


def getdata(database_name, value):
    lis = querydb(database_name)
    data_list = []
    if value == "value":
        for each in lis:
            data_list.append(each["value"])
    else:
        for each in lis:
            data_list.append(each["name"])
    return data_list


@app.route('/')
def my_map():
    aurindata = querydb("aurin_richness")
    lustdata = querydb("lust_web")
    pridedata = querydb("pride_web")

    return render_template('map.html', aurindata=json.dumps(aurindata), lustdata=json.dumps(lustdata),
                           pridedata=json.dumps(pridedata))


@app.route('/linechart')
def my_linechart():

    aurindata = getdata("aurin_richness", "value")

    lustdata = getdata("lust_web", "value")

    pridedata = getdata("pride_web", "value")

    xlabel = getdata("aurin_richness", "name")

    return render_template('linechart.html', aurindata=aurindata, lustdata=lustdata,
                           pridedata=pridedata, xlabel=xlabel)


class Datasource(Resource):
    def get(self, name):
        meta_data = []
        aurin = {}
        aurin["name"] = "richness"
        aurin["data"] = querydb("aurin_richness")
        meta_data.append(aurin)

        lustdata = {}
        lustdata["name"] = "lust"
        lustdata["data"] = querydb("lust_web")
        meta_data.append(lustdata)

        pridedata = {}
        pridedata["name"] = "pride"
        pridedata["data"] = querydb("pride_web")
        meta_data.append(pridedata)
        for data in meta_data:
            if name == data["name"]:
                return data, 200
        return "Data not found", 404


api.add_resource(Datasource, "/data/<string:name>")


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug = True)





