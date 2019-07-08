# Basic Flask based Web UI with user auth

Using:
Python 3.6+
Flask
Flask-User
SQLAlchemy

What it is:
Basic web UI with basic front page and user management.
Front page will have a login button where people log in.

How to run:

* Make sure Python 3.6+ and Git is installed on your PC
* Download app into a folder on your PC with:
`git clone https://DanieCornelius@bitbucket.org/DanieCornelius/tdb.git`

Open a comand prompt and change directory into that folder.

Then run:
* `py -3 -m venv venv`
    * (This installs the Python Virual Environment in the project folder)
* `venv\scripts\activate`
    * (This activates the virtual environment)
* `pip install -r requirements.txt`
    * (This installs all the requirements needed to run our app)
    * Create a new file called settings.py in the clientapp folder
    * In this file add the following settings
        * SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

* `set FLASK_APP=clientapp`
* `flask run`
    * (The app is now running and you can connect to it using the address and port provided in your browser)


Press `Control-C` to stop running the program.
Type `deactivate` to exit the virtual environment.
