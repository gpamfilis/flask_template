export FLASK_APP=manage.py
export FLASK_ENV=development
# sh flask_env.sh
flask db init
flask db migrate
flask db upgrade
flask run -h 0.0.0.0
