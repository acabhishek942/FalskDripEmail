from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    unique_id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    campaigns = db.relationship('Campaign', backref = 'user', lazy = True)

    def __repr__(self):
      return '<User %r>' % self.email


class Campaign(db.Model):
    unique_id = db.Column(db.String, primary_key=True)
    title  = db.Column(db.String(120), unique=True, nullable=False)
    stages = db.Column(db.Integer, nullable = False)
    frequency =  db.Column(db.Integer, nullable = False) #needs-attention
    recipients =  db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.unique_id'), nullable=False)


class Email(db.Model):
    unique_id = db.Column(db.String, primary_key=True)
    subject =  db.Column(db.String(200), nullable = False)
    body  = db.Column(db.Text, nullable =  False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.unique_id'),  nullable=False)
