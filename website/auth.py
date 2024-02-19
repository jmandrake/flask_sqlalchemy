from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, try again.", category='error')
        else:
            flash("Email does not exist.", category='error')
    return render_template("login.html")

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        print(data)
        email = data['email']
        password1 = data['password']
        password2 = data['password2']
        username = data['username']
        print(username, email, password1, password2)
        # check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            print("User already exists")
            flash("User already exists", category='error')
        else:
            # check user input
            if len(email) < 4:
                print("Email must be greater than 4 characters")
                flash("Email must be greater than 4 characters", category='error')
            elif len(username) < 2:
                print("Username must be greater than 2 characters")
                flash("Username must be greater than 2 characters", category='error')
            elif password1 != password2:
                print("Passwords don't match")
                flash("Passwords don't match", category='error')
            else:
                print("Data is valid")
                # create new user
                # new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
                new_user = User(email=email, username=username, password=generate_password_hash(password1, method='pbkdf2:sha256'))

                db.session.add(new_user) # add the user to the database
                db.session.commit()
                flash("Account created!", category='success')
                return redirect(url_for('views.home'))


    return render_template("sign_up.html")

@auth.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    return "<p>Reset Password</p>"