from flask import render_template, session, redirect, url_for
from . import main
from app import db
from app.models import User

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@main.route('/', methods=['GET', 'POST'])
def home():
    """Render website's home page."""
    return render_template('main/index.html')

@main.route('login')
def add_user():
    user = User(email = id_generator(),username=id_generator())
    db.session.add(user)
    db.session.commit()
    return render_template('main/index.html')

def randString():
    return ''.join(random.choice())
