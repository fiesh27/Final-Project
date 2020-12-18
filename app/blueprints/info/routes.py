from . import bp as info
from flask import render_template

@info.route('/about_us')
def about_us():
    return render_template('aboutus.html')
