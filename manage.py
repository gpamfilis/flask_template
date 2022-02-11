import os

from app import create_app, db
print('Running manage.py')

from app.models import User

# from flask_script import Manager, Shell
from flask_migrate import Migrate

environment = os.getenv('FLASK_ENV') or 'development'
print('Environment: ', environment)
app = create_app(environment)


# manager = Manager(app)
migrate = Migrate(app, db, compare_type=True)


def make_shell_context():
    return dict(app=app, db=db, User=User)


# manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    print(app)
    app.run()
