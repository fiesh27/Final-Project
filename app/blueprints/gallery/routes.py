import os

from . import bp as gallery

from flask import render_template, url_for

@gallery.route('/gallery')
def gallery():
#     return render_template('gallery.html')

# def photos(): 
    # basedir = os.path.abspath(os.path.dirname(__file__)) 
    pics = os.listdir('app/static/images')  
    return render_template("gallery.html", pics=pics)  

 