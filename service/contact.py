from models.contacts import Contact
from utils.db import db


class ContactService:
    @staticmethod
    def create_contact(data):
        full_name = data.get('full_name')
        email = data.get('email')
        phone = data.get('phone')

        if not all([full_name, email, phone]):
            return {'message': 'Faltan campos obligatorios'}, 400

        new_contact = Contact(full_name=full_name, email=email, phone=phone)
        db.session.add(new_contact)
        db.session.commit()

        return {'message': 'Contacto creado exitosamente'}, 201

    @staticmethod
    def get_contact_by_id(contact_id):
        contact = Contact.query.get(contact_id)
        if not contact:
            return {'message': 'Contacto no encontrado'}, 404
        return contact.serialize(), 200

    @staticmethod
    def get_all_contacts():
        contacts = Contact.query.all()
        return [contact.serialize() for contact in contacts], 200

    @staticmethod
    def update_contact(contact_id, data):
        contact = Contact.query.get(contact_id)
        if not contact:
            return {'message': 'Contacto no encontrado'}, 404

        full_name = data.get('full_name')
        email = data.get('email')
        phone = data.get('phone')

        if full_name:
            contact.full_name = full_name
        if email:
            contact.email = email
        if phone:
            contact.phone = phone

        db.session.add(contact)
        db.session.commit()

        return {'message': 'Contacto actualizado exitosamente'}, 200

    @staticmethod
    def delete_contact(contact_id):
        contact = Contact.query.get(contact_id)
        if not contact:
            return {'message': 'Contacto no encontrado'}, 404

        db.session.delete(contact)
        db.session.commit()

        return {'message': 'Contacto eliminado exitosamente'}, 200
