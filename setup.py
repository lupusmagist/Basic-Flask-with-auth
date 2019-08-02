import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="BasicUI",
    version="1.0.0",
    url="https://github.com/lupusmagist/Basic-Flask-with-auth",
    license="MIT",
    maintainer="D. Cornelius",
    maintainer_email="lupusmagist@gmail.com",
    description="Basic UI template using Flask",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask', 'flask-user',
                      'flask-sqlalchemy', 'flask-migrate', ],
    extras_require={"test": ["pytest", "coverage"]},
)
