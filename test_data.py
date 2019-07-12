import logging
# import os

from mainapp import create_app
from mainapp import db
from mainapp.auth.models import User, Role
from mainapp.auth import bcrypt
from settings import DevConfig


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

log = logging.getLogger(__name__)

# env = os.environ.get('APP_ENV', 'dev')
# app = create_app('settings.%sConfig' % env.capitalize())

app = create_app(DevConfig)
app.app_context().push()


fake_users = [
    {'username': 'user', 'role': 'user'},
    {'username': 'admin', 'role': 'admin'}
]
fake_roles = ['user', 'admin']


def generate_roles():
    roles = list()
    for rolename in fake_roles:
        role = Role.query.filter_by(name=rolename).first()
        if role:
            roles.append(role)
            continue
        role = Role(rolename)
        roles.append(role)
        db.session.add(role)
        try:
            db.session.commit()
        except Exception as e:
            log.error("Erro inserting role: %s, %s" % (str(role), e))
            db.session.rollback()
    return roles


def generate_users():
    users = list()
    for item in fake_users:
        user = User.query.filter_by(username=item['username']).first()
        if user:
            users.append(user)
            continue
        user = User()
        user.username = item['username']
        user.password = bcrypt.generate_password_hash("password")
        users.append(user)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            log.error("Eror inserting user: %s, %s" % (str(user), e))
            db.session.rollback()
    return users


generate_roles()
generate_users()
