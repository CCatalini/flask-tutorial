from flask import Blueprint, jsonify, request
from exceptions import AlreadyExistsError
from exceptions import NotFoundError

user_bp = Blueprint('user_bp', __name__)
users = [1, 2, 3, 4, 5]


@user_bp.route('/user')
def user():
    return 'User'


# @user_bp.route('/user', methods=['POST'])
# def create_user(self):
#     data = request.json
#     try:
#         new_user = self.user_service.create_user(data)
#         # return jsonify(new_user.serialize()), 201
#         return jsonify({
#             'id': new_user.id,
#             'email': new_user.email,
#             'token': new_user.token
#         }), 201
#     except AlreadyExistsError as e:
#         return jsonify(e.message), 400
#
#     def get_user(self, user_id):
#         try:
#             user = self.user_service.get_user_by_id(user_id)
#             return jsonify(user.serialize()), 200
#         except NotFoundError as e:
#             return jsonify(e.message), 404
#
#     def get_users(self):
#         users = self.user_service.get_users()
#         return jsonify([user.serialize() for user in users]), 200
#
#     def update_user(self, user_id):
#         # request.json should be in the form of the DTO user_update_dto
#         input_dto = request.json
#         try:
#             updated_user = self.user_service.update_user(user_id, input_dto)
#             return jsonify(updated_user.serialize()), 200
#         # NotFoundError is raised in the service when the user is not found
#         except NotFoundError as e:
#             return jsonify(e.message), 404
#
#     def delete_user(self, user_id):
#         try:
#             self.user_service.delete_user(user_id)
#             return jsonify({"message": "User deleted successfully"}), 200
#         except NotFoundError as e:
#             return jsonify(e.message), 404
#
#
# def register_routes(app: Flask, user_controller: UserController):
#     app.add_url_rule('/users', methods=['POST'], view_func=user_controller.create_user)
#     app.add_url_rule('/users/<int:user_id>', methods=['GET'], view_func=user_controller.get_user)
#     app.add_url_rule('/users/<int:user_id>', methods=['DELETE'], view_func=user_controller.delete_user)
#     app.add_url_rule('/users/<int:user_id>', methods=['PUT'], view_func=user_controller.update_user)
#
#
# @user_bp.route('/user/<int:id>', methods=['DELETE'])  # delete user
# def delete_user(id):
#     if id in users:
#         users.remove(id)
#         return jsonify({'message': 'User deleted successfully'})
#     else:
#         return jsonify({'error': 'User not found'}), 404
#