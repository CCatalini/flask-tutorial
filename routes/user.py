from flask import Blueprint, jsonify, request
from exceptions import AlreadyExistsError
from exceptions import NotFoundError
from service.user import UserService

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/user')
def user():
    return 'User'


@user_bp.route('/user', methods=['POST'])
def create_user():
    result, status_code = UserService.create_user(request.json)
    return jsonify(result), status_code


@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_contact(user_id):
    result, status_code = UserService.get_user_by_id(user_id)
    return jsonify(result), status_code


@user_bp.route('/users', methods=['GET'])
def all_contacts():
    result, status_code = UserService.get_all_users()
    return jsonify(result), status_code


@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_contact(user_id):
    data = request.json
    result, status_code = UserService.update_user(user_id, data)
    return jsonify(result), status_code


@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_contact(user_id):
    result, status_code = UserService.delete_user(user_id)
    return jsonify(result), status_code
