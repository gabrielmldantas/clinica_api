from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

import clinica.models
import clinica.views.crud

if db.session.query(clinica.models.Usuario).filter(clinica.models.Usuario.username=='admin').count() == 0:
    usuario_admin = clinica.models.Usuario()
    usuario_admin.nome = 'Admin'
    usuario_admin.username = 'admin'
    usuario_admin.senha = generate_password_hash('admin')
    usuario_admin.email = 'admin@clinicaddm.com.br'
    db.session.add(usuario_admin)
    db.session.commit()