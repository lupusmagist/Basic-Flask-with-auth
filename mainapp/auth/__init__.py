import functools
from flask import abort
from flask_login import current_user
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_login import AnonymousUserMixin


class AnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


bcrypt = Bcrypt()
login_manager = LoginManager()
# login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"
login_manager.anonymous_user = AnonymousUser


def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .views import auth_blueprint
    app.register_blueprint(auth_blueprint)


def has_role(name):
    def real_decorator(f):
        def wraps(*args, **kwargs):
            if current_user.has_role(name):
                return f(*args, **kwargs)
            else:
                abort(403)
        return functools.update_wrapper(wraps, f)
    return real_decorator


@login_manager.user_loader
def load_user(userid):
    from .models import User
    return User.query.get(userid)
