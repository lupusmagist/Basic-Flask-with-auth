from setuptools import setup

setup(
    name='BasicUI',
    python_requires='>=3.6',
    install_requires=['flask==1.0.2', 'flask-user==1.0.1.5',
                      'flask-sqlalchemy==2.3.2', 'flask-migrate==2.5.2', ],
)
