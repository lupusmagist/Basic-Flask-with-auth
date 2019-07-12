from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from ..auth.forms import LoginForm
# from ..auth.models import User
# from ..auth import has_role

admin_blueprint = Blueprint(
    'admin', __name__, template_folder='../templates/admin',
    url_prefix="/admin")


@admin_blueprint.route('/')
def index():
    return render_template('admin/index.html')
