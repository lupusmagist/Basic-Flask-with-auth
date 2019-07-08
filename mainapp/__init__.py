from .settings import DevConfig
from flask import Flask, session
from flask_migrate import Migrate, MigrateCommand
from flask.sessions import SessionInterface
from flask_sqlalchemy import SQLAlchemy
from flask_user import user_logged_out, UserManager, current_user
from flask_wtf.csrf import CSRFProtect


# Instantiate Flask extensions
db = SQLAlchemy()
csrf_protect = CSRFProtect()
migrate = Migrate()

from mainapp.models.models import User


def get_config():
    # Instantiate Flask
    app = Flask(__name__)

    # Load App Config settings
    # Load common settings from 'app/settings.py' file
    app.config.from_object(DevConfig)
    return app.config


def create_app():
    ''' The main flask app
    '''
    app = Flask(__name__)
    # Load config settings
    base_config = get_config()
    app.config.update(base_config)

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Setup WTForms CSRFProtect
    csrf_protect.init_app(app)

    # Setup Flask-User and specify the User data-model
    UserManager(app, db, User)

    # Register blueprints
    from mainapp.views.main import main_blueprint
    app.register_blueprint(main_blueprint)

    from mainapp.views.admin import admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
