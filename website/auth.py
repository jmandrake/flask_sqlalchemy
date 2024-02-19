from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
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
            flash("Account created!", category='success')




    return render_template("sign_up.html")

@auth.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    return "<p>Reset Password</p>"