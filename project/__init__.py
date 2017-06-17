# project/__init__.py
import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

# set config with docker env settings
app_setting = os.getenv('APP_SETTINGS')
app.config.from_object(app_setting)

# instantiate the db
db = SQLAlchemy(app)

# model
class User(db.Model):
        __tableusers_ = "users"
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(128), nullable=False)
        email = db.Column(db.String(128), nullable=False)
        active = db.Column(db.Boolean(), default=False, nullable=False)
        created_at = db.Column(db.DateTime, nullable=False)

        def __int__(self, username, email):
            self.username = username
            self.email = email
            self.created_at = datetime.datetime.now()

# routes

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'sucess',
        'message': 'pong!'
    })

