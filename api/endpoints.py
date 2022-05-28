from flask import render_template, Response, request
from flask_cors import cross_origin
from api import api, db
from api.models import Candidate

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
        dict = request.get_json(force=True)
        try:
            db.session.add(Candidate(**dict))
            db.session.commit()
            return Response(status=201)
        except:
            return Response(status=202)