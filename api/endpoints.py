from flask import render_template, jsonify, Response, request
from flask_cors import cross_origin
from api import api

@api.route('/')
def index_route():
    return render_template('index.html')

@api.route(
    '/api/recruitment',
    methods=['POST', 'GET']
)
def recruitment_route():
    if request.method == 'GET':
        return 'POST HERE'
    if request.method == 'POST':
        return Response(201)