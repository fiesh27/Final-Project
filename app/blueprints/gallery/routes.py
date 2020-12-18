from . import bp as gallery

from flask import render_template, url_for

@gallery.route('/gallery')
def gallery():
    
    images = url_for('static', filename = 'images/pic06.jpg')
    
    return render_template('gallery.html', filename=images)