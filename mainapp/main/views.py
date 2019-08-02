from flask import Blueprint, render_template, flash, redirect, url_for, \
    request, session
from flask_login import login_user, login_required
from ..auth.forms import LoginForm
from ..auth.models import User
# from ..auth import has_role

main_blueprint = Blueprint(
    'main', __name__, template_folder='../templates/main')


@main_blueprint.before_request
def make_session_permanent():
    session.permanent = False


@main_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = LoginForm(request.form)

    return render_template('index.html', form=form)
