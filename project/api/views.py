#project/api/views.py

from flask import Blueprint, jsonify, request, make_response
from project.api.models import User
from project import db
from sqlalchemy import exc

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@users_blueprint.route('/users', methods=['POST'])
def add_user():
    post_data = request.get_json()
    # handler the empty post
    if not post_data:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }

        # 返回
        return make_response(jsonify(response_object)), 400
    username = post_data.get('username')
    email = post_data.get('email')
    try:
        # handler the duplicate email post
        user = User.query.filter_by(email=email).first()

        # not duplicate email
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()

            response_object = {
                'status': 'success',
                'message': f'{email} was added!'
            }
            return make_response(jsonify(response_object)), 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry, That email has already exist.'
            }
            return make_response(jsonify(response_object)), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return make_response(jsonify(response_object)), 400





