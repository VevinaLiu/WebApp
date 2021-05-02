

from flask import render_template, url_for, redirect, session
from myproject import app



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/help')
def helppage():
    return render_template('helppage.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
