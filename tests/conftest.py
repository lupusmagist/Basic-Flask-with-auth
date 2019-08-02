import os
import pytest
import sqlite3

from mainapp import create_app, db as _db
from settings import TestConfig

basedir = os.path.abspath(os.path.dirname(__file__))

# Thank you ALEX MICHAEL http://alexmic.net/flask-sqlalchemy-pytest/
@pytest.fixture(scope='session')
def app(request):
    app = create_app(TestConfig)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app, request):

    def teardown():
        _db.drop_all()
        # os.unlink(TestConfig.SQLALCHEMY_DATABASE_URI)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    # ! Loading sql data from file before usign the session.
    f = open(basedir + '/db.sql')
    script_str = f.read().strip()
    session.close()
    conn = sqlite3.connect(os.path.join(basedir, 'test_db.db'))
    conn.executescript(script_str)
    conn.commit()

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
