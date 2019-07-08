from setuptools import setup

setup(
    name = 'BasicUI',
    python_requires='>=3.6',
    install_requires = ['flask','flask-user','flask-sqlalchemy','flask-migrate', 'beaker',],
)
