import os
from mainapp import create_app

env = os.environ.get('APP_ENV', 'dev')
app = create_app('settings.%sConfig' % env.capitalize())


if __name__ == '__main__':
    app.run()
