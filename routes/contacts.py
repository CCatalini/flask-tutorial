from flask import jsonify, request, Blueprint, Flask

from models.contacts import Contact
from utils.db import db

contacts_bp = Blueprint('contacts_bp', __name__)


@contacts_bp.route('/')
def home():
    return 'Contacts home'


@contacts_bp.route('/new', methods=['POST'])
def new_contact():
    data = request.json

    # Extraer datos del JSON
    full_name = data.get('full_name')
    email = data.get('email')
    phone = data.get('phone')

    # Verificar si todos los campos están presentes
    if not all([full_name, email, phone]):
        return jsonify({'message': 'Faltan campos obligatorios'}), 400

    new_contact = Contact(full_name=full_name, email=email, phone=phone)

    # Agregar el nuevo contacto a la base de datos
    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Contacto creado exitosamente'}), 201
