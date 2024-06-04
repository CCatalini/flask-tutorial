from flask import jsonify, request, Blueprint, Flask

from models.contacts import Contact
from service.contact import ContactService
from utils.db import db

contacts_bp = Blueprint('contacts_bp', __name__)


@contacts_bp.route('/')
def home():
    return 'Contacts home'


@contacts_bp.route('/new', methods=['POST'])
def new_contact():
    result, status_code = ContactService.create_contact(request.json)
    return jsonify(result), status_code


@contacts_bp.route('/contact/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    result, status_code = ContactService.get_contact_by_id(contact_id)
    return jsonify(result), status_code


@contacts_bp.route('/all-contacts', methods=['GET'])
def all_contacts():
    result, status_code = ContactService.get_all_contacts()
    return jsonify(result), status_code


@contacts_bp.route('/contact/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.json
    result, status_code = ContactService.update_contact(contact_id, data)
    return jsonify(result), status_code


@contacts_bp.route('/contact/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    result, status_code = ContactService.delete_contact(contact_id)
    return jsonify(result), status_code
