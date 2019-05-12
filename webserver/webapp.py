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

app = Flask(__name__)


def getdb(database_name):
    couch = couchdb.Server('http://admin:admin@172.26.38.106:5984')
    db = couch[database_name]
    return db


def querydb(database_name):
    db = getdb(database_name)
    lis = []
    for each in db:
        doc = db[each]
        content = {}
        if doc['name'] == 'mckinnon':
            content['name'] = 'McKinnon'
        else:
            content['name'] = doc['name'].title()
        content['value'] = doc['score']
        lis.append(content)
    return lis


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
    aurindata = querydb("aurin_uni")
    lustdata = [
            {'name': 'Cremorne', 'value': 0.3},
            {'name': 'Caulfield', 'value': 0.6},
            {'name': 'Carnegie', 'value': 0.55},
            {'name': 'Kingsville', 'value': 0.55}]

    pridedata = [
        {'name': 'Cremorne', 'value': 0.5},
        {'name': 'Caulfield', 'value': 0.3},
        {'name': 'Carnegie', 'value': 0.44},
        {'name': 'Kingsville', 'value': 0.8}]

    return render_template('map.html', aurindata=json.dumps(aurindata), lustdata=json.dumps(lustdata),
                           pridedata=json.dumps(pridedata))


@app.route('/linechart')
def my_linechart():

    aurindata = getdata("aurin_uni", "value")


    lustdata = [0.3, 0.6, 0.55, 0.55]

    pridedata = [0.5, 0.3, 0.44, 0.8]

    xlabel = getdata("aurin_uni", "name")

    return render_template('linechart.html', aurindata=aurindata, lustdata=lustdata,
                           pridedata=pridedata, xlabel=xlabel)


@app.route('/data')
def my_data():
    meta_data ={}
    meta_data["aurin data"] = querydb("aurin_uni")
    meta_data["twitter_data"] = [
            {'name': 'Cremorne', 'value': 0.3},
            {'name': 'Caulfield', 'value': 0.6},
            {'name': 'Carnegie', 'value': 0.55},
            {'name': 'Kingsville', 'value': 0.55}]
    meta_data["instagram data"] = [
        {'name': 'Cremorne', 'value': 0.5},
        {'name': 'Caulfield', 'value': 0.3},
        {'name': 'Carnegie', 'value': 0.44},
        {'name': 'Kingsville', 'value': 0.8}]
    return jsonify(meta_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


