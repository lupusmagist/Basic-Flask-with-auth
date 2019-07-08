from flask import Blueprint, render_template, request
from mainapp.forms.main_forms import LoginForm

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_index():
    form = LoginForm(request.form)
    return render_template('index.html', form=form)
