from flask import Flask, render_template
import json
import couchdb

app = Flask(__name__)

def getdoc(database_name):
    couch = couchdb.Server('http://localhost:5984')
    db = couch[database_name]
    doc = db['069f17f9c6efd0038affffecda0020c3']
    return doc


def querydb(database_name):
    doc = getdoc(database_name)
    lis = []
    for i in range(122):
        i += 1
        order = str(i)
        content = {}
        if doc[order]['name'] == 'mckinnon':
            content['name'] = 'McKinnon'
        else:
            content['name'] = doc[order]['name'].title()
        content['value'] = doc[order]['count']
        lis.append(content)
    return lis


def getdata(database_name, value):
    doc = querydb(database_name)
    data_list = []
    if value == "value":
        for each in doc:
            data_list.append(each["value"])
    else:
        for each in doc:
            data_list.append(each["name"])
    return data_list

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map')
def my_map():
    twitterdata = querydb("twitter")
    aurindata = [
        {'name': 'Cremorne', 'value': 0.97453},
        {'name': 'Caulfield', 'value': 20},
        {'name': 'Carnegie', 'value': 50},
        {'name': 'Kingsville', 'value': 60}]

    instagramdata = [
        {'name': 'Cremorne', 'value': 200},
        {'name': 'Caulfield', 'value': 300},
        {'name': 'Carnegie', 'value': 0.3438332},
        {'name': 'Kingsville', 'value': 700}]

    return render_template('map.html', twitterdata=json.dumps(twitterdata), aurindata=json.dumps(aurindata),
                           instagramdata=json.dumps(instagramdata))


@app.route('/linechart')
def my_linechart():

    twitterdata = getdata("twitter", "value")

    aurindata = [100, 20, 50, 60]
    instagramdata = [20, 100, 300, 30]

    xlabel = getdata("twitter", "name")

    return render_template('linechart.html', twitterdata=twitterdata, aurindata=aurindata,
                           instagramdata=instagramdata, xlabel=xlabel)


if __name__ == "__main__":
    app.run(debug = True)
    #app.run(use_reloader=True)
#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0')