from .. import db
from . import AnonymousUserMixin

roles = db.Table(
    'role_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False,
                         index=True, unique=True)
    password = db.Column(db.String(255))

    roles = db.relationship(
        'Role',
        secondary=roles,
        backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username, password):
        # default role is 'user' and it added automaticly
        default = Role.query.filter_by(name="user").one()
        self.roles.append(default)
        self.username = username
        self.password = password

    def has_role(self, name):
        for role in self.roles:
            if role.name == name:
                return True
        return False

    # Methods for loginmanager/flask-user
    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

    '''
    def __init__(self, username=""):
        default = Role.query.filter_by(name="user").one()
        self.roles.append(default)
        self.username = username

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def has_role(self, name):
        for role in self.roles:
            if role.name == name:
                return True
        return False

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    '''


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role {}>'.format(self.name)
