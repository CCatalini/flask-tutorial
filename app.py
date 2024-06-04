from flask import Flask
from routes.user import user_bp
from routes.contact import contacts_bp

from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask-tutorial-bd'

db.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(contacts_bp)
