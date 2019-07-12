from flask import (render_template,
                   Blueprint,
                   redirect,
                   url_for,
                   flash,
                   request,)
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
    form = LoginForm()
    if request.method == 'GET':
        return render_template('main/index.html', form=form)
    if request.method == 'POST' and form.validate_on_submit():
        registered_user = User.query.filter_by(
            username=form.username.data).first()
        if registered_user:
            if bcrypt.check_password_hash(
                    registered_user.password, form.password.data):
                if form.remember_me.data:
                    login_user(registered_user, remember=True)
                    flash('Logged in successfully')
                    return redirect(url_for('admin.index'))
                else:
                    login_user(registered_user)
                    flash('Logged in successfully')
                    return redirect(url_for('admin.index'))
            else:
                flash('Password is invalid', 'error')
                return redirect(url_for('index'))
        else:
            flash('Username is invalid', 'error')
            return redirect(url_for('index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(u"Error in the %s field - %s" %
                      (getattr(form, field).label.text, error))

        return render_template('main/index.html', form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You have been logged out.", category="info")
    return redirect(url_for('main.index'))
