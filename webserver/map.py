#coding:utf-8

from flask import Flask,render_template,url_for


app = Flask(__name__)

@app.route('/')
def my_map():
    return render_template('map.html')

@app.route('/linechart')
def my_linechart():
    return render_template('linechart.html')

if __name__ == "__main__":
    #运行项目
    #app.run(debug = True）
    app.run(use_reloader=True)

