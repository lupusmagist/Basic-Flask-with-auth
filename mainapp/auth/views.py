from flask import (render_template,
                   Blueprint,
                   redirect,
                   url_for,
                   flash,)
from . import bcrypt
from .models import User
from .forms import LoginForm
from flask_login import login_user, logout_user


auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    url_prefix="/auth"
)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                # user should be an instance of your `User` class
                login_user(user)
                flash('Logged in successfully.')

                return redirect(url_for('main.index'))
            else:
                flash('Login Failed')

    return render_template('auth/login.html', form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You have been logged out.", category="info")
    return redirect(url_for('main.index'))
