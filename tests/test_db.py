from mainapp.auth.models import Role, User
from mainapp.auth import bcrypt


def test_role_schema1(session):
    test_role_user = Role.query.filter_by(name='user').first()
    test_role_admin = Role.query.filter_by(name='admin').first()

    assert test_role_user.name == 'user'
    assert test_role_admin.name == 'admin'


def test_user_schema1(session):
    passwd = bcrypt.generate_password_hash("password")
    new_user = User(username='foo', password=passwd)

    session.add(new_user)
    session.commit()

    assert new_user.username == 'foo'
    test_new_user = User.query.filter_by(username='foo').first()

    assert test_new_user.username == 'foo'
