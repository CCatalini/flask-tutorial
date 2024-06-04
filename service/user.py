from models.user import User
from utils.db import db


class UserService:

    @staticmethod
    def create_user(data):
        email = data.get('email')
        password = data.get('password')
        profile_pic_url = data.get('profile_pic_url')

        if not all([email, password]):
            return {'message': 'Faltan campos obligatorios'}, 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {'message': 'El correo electronico ya esta en uso'}, 400

        new = User(email=email, password=password, profile_pic_url=profile_pic_url)
        db.session.add(new)
        db.session.commit()

        return {'message': 'Usuario creado exitosamente'}, 201

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'Usuario no encontrado'}, 404
        return user.serialize(), 200

    @staticmethod
    def get_all_users():
        users = User.query.all()
        return [user.serialize() for user in users], 200

    @staticmethod
    def update_user(user_id, data):
        # el id de usuario deberíamos obtenerlo del token
        user = User.query.get(user_id)
        if not user:
            return {'message': 'Usuario no encontrado'}, 404

        email = data.get('email')
        password = data.get('password')
        profile_pic_url = data.get('profile_pic_url')

        if email:               user.email = email
        if password:            user.password = password
        if profile_pic_url:     user.profile_pic_url = profile_pic_url

        db.session.add(user)
        db.session.commit()

        return {'message': 'Usuario actualizado exitosamente'}, 200

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'Usuario no encontrado'}, 404

        db.session.delete(user)
        db.session.commit()

        return {'message': 'Usuario eliminado exitosamente'}, 200
