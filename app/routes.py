from flask import current_app as app, render_template, url_for, redirect


@app.route('/')
def index():
    return redirect(url_for('intro.index'))


