from app import app
from flask import render_template



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/one')
def onecol():
    return render_template('onecolumn.html')

@app.route('/two_1')
def twocol_1():
    return render_template('twocolumn1.html')

@app.route('/twocol_2')
def twocol_2():
    return render_template('twocolumn2.html')

@app.route('/threecol')
def threecol():
    return render_template('threecolumn.html')

