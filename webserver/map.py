from flask import Flask,render_template
import json
import couchdb

app = Flask(__name__)


def getDoc(database_name):
    couch = couchdb.Server('http://Yanli:muzifeng1021@127.0.0.1:5984')
    db = couch[database_name]
    doc = db['0d99472d9fd2d79461528599f304bccb']
    return doc

def queryDb(database_name):
    doc = getDoc(database_name)
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

def getData(database_name, value):
    doc = queryDb(database_name)
    data_list = []
    if value == "value":
        for each in doc:
            data_list.append(each["value"])
    else:
        for each in doc:
            data_list.append(each["name"])
    return data_list


@app.route('/')
def my_map():
    twitterdata = queryDb("twitter")
    aurindata = [
        {'name': 'Cremorne', 'value': 100},
        {'name': 'Caulfield', 'value': 20},
        {'name': 'Carnegie', 'value': 50},
        {'name': 'Kingsville', 'value': 60}]

    instagramdata = [
        {'name': 'Cremorne', 'value': 200},
        {'name': 'Caulfield', 'value': 300},
        {'name': 'Carnegie', 'value': 500},
        {'name': 'Kingsville', 'value': 700}]

    return render_template('map.html', twitterdata=json.dumps(twitterdata), aurindata=json.dumps(aurindata),
                           instagramdata=json.dumps(instagramdata))



@app.route('/linechart')
def my_linechart():


    twitterdata = getData("twitter", "value")

    aurindata = [100, 20, 50, 60]
    instagramdata = [20, 100, 300, 30]

    xlabel = getData("twitter", "name")

    return render_template('linechart.html', twitterdata=twitterdata, aurindata=aurindata,
                           instagramdata=instagramdata, xlabel=xlabel)


if __name__ == "__main__":
    app.run(debug = True)
    #app.run(use_reloader=True)

