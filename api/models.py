from api import db

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=True)
    whatLinux = db.Column(db.Text, nullable=False, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    flagCommad = db.Column(db.String(128), nullable=False, unique=False)