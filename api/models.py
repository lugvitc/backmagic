from api import db

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String, nullable=False, unique=False)
    contact = db.Column(db.String, nullable=False, unique=False)
    prefDept = db.Column(db.String, nullable=False, unique=False)
    regno = db.Column(db.String, nullable=False, unique=False)
    whatLinux = db.Column(db.String, nullable=False, unique=False)
    whyLinux = db.Column(db.String, nullable=False, unique=False)
    expLinux = db.Column(db.String, nullable=False, unique=False)
    flagCommad = db.Column(db.String, nullable=False, unique=False)