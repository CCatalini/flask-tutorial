## This file contains the routes for the Zelmira users entity

from flask import Blueprint, jsonify, request, Flask

user_bp = Blueprint('user_bp', __name__)
users = [1, 2, 3, 4, 5]


@user_bp.route('/user')
def user():
    return 'User'


@user_bp.route('/user', methods=['POST'])  # create user
def create_user():
    data = request.json
    users.append(data['id'])
    return jsonify({'message': 'User created'}), 201


@user_bp.route('/user/<int:id>', methods=['GET'])  # get user
def get_user(id):
    if id in users:
        return jsonify({'id': id})
    else:
        return jsonify({'error': 'User not found'}), 404


@user_bp.route('/users', methods=['GET'])  # get all users
def get_users():
    return jsonify({'users': users})


@user_bp.route('/user/<int:id>', methods=['PUT'])  # update user
def update_user(id):
    if id in users:
        users.remove(id)
        data = request.json
        users.append(data)
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404


@user_bp.route('/user/<int:id>', methods=['DELETE'])  # delete user
def delete_user(id):
    if id in users:
        users.remove(id)
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404
