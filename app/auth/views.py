from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import User
from .forms import LoginForm, RegistrationForm
from .. import db


# from firebase import firebase
# import flask_featureflags as feature

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # check if the form fields are valid
        # set the first result from the query equal to user
        user = User.query.filter_by(email=form.email.data).first()
        # if the user variable is not None (meaning the query found the username) and the password passed to the form
        # matches the password of the user
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            # redirect them to the index.html page or if a user had clicked on a link before login that required login.
            # and redirected him to log in. send him to that page.
            flash('You have been logged in.')
            return redirect(request.args.get('next') or url_for('main.home'))
        # if all goes to hell just flash him a message that tells him that either the username or password is Invalid.
        flash('Invalid username or password.')
    # if the form is not valid on submit then simply redirect him to the same page (/auth/login.html) to try again etc.
    return render_template('auth/login.html', form=form)


# TODO

@auth.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.home'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form)
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.flush()

        db.session.commit()

        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
