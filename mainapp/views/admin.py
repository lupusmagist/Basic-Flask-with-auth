from flask import Blueprint

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/admin/')
def admin_index():
    return 'admin index'
