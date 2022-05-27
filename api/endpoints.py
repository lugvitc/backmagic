from flask import render_template

from api import api

@api.route('/')
def index_route():
    return render_template('index.html')