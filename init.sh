if [ ! -d "venv" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    python3 -m venv venv
fi
source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=main.py
if [ ! -d "migrations" ]; then
    echo --------------------
    echo INIT THE migrations folder
    echo --------------------
    export FLASK_APP=main.py; flask db init
fi
echo --------------------
echo Generate migration DDL code
echo --------------------
flask db migrate
echo --------------------
echo Run the DDL code and migrate
echo --------------------
echo --------------------
echo This is the DDL code that will be run
echo --------------------
flask db upgrade
if [ ! -f "settings.py" ]; then
    echo --------------------
    echo Creating settings.py file
    echo --------------------
    cat <<EOF > settings.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():

    # Application settings
    APP_NAME = "Basic UI"

    # Flask User settings
    CSRF_ENABLED = True

    # Flask-User settings
    USER_APP_NAME = APP_NAME
    USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
    USER_ENABLE_CHANGE_USERNAME = False  # Allow users to change their username
    USER_ENABLE_CONFIRM_EMAIL = False  # Force users to confirm their email
    USER_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
    USER_ENABLE_EMAIL = False  # Register with Email
    USER_ENABLE_REGISTRATION = False  # Allow new users to register
    USER_REQUIRE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
    USER_ENABLE_USERNAME = False  # Register and Login with username
    USER_AFTER_LOGIN_ENDPOINT = 'main.member_page'
    USER_AFTER_LOGOUT_ENDPOINT = 'main.member_page'
    USER_ALLOW_LOGIN_WITHOUT_CONFIRMED_EMAIL = False
    REMEMBER_COOKIE_DURATION = 432000  # Remeber login for 5 days.(Seconds)


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True
    # Flask-SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SECRET_KEY = '\x19\xbe\x9a^\x93\xf5\xcb\x00i\x07\x99\x8e$r\xfe\xf6'

EOF
fi
