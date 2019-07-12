from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Instantiate Flask extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app(object_name):
    ''' The main flask app
    '''
    app = Flask(__name__)
    app.config.from_object(object_name)

    # Setup Database
    db.init_app(app)
    migrate.init_app(app, db)

    from .auth import create_module as auth_create_module
    auth_create_module(app)

    # Register blueprints
    from .main.views import main_blueprint
    app.register_blueprint(main_blueprint)
    app.add_url_rule('/', endpoint='index')

    from .admin.views import admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
