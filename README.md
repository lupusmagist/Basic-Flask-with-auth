# Basic Flask based Web UI with user authentication

Using:
Python 3.6+
Flask
Flask-User
Flask-SQLAlchemy

What it is:
Basic web UI with basic front page and user management.
Front page will have a login button where people log in.

Logging in will redirect the user to another area.

Can be used as a starting template for other projects.

How to run:

* Make sure Python 3.6+ and Git is installed on your PC
* Download app into a folder on your PC with:
`https://github.com/lupusmagist/Basic-Flask-with-auth.git`

Open a command prompt and change directory into that folder.

Then run:
* `./init.sh`
    * This command will create the virtual environment, install requirements, setup the database and create the settings.py file.

If some data is needed in the database:
* `source venv/bin/activate`
* `python test_data.py`

To run the app, either:
* `./run.sh`
* or
* `source venv/bin/activate`
* `export FLASK_APP=main`
* `export FLASK_ENV=development`
* `flask run`

* (The app is now running and you can connect to it using the address and port provided in your browser)

Press `Control-C` to stop running the program.
Type `deactivate` to exit the virtual environment.
