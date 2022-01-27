from crypt import methods
from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask_app.models.recipe import Recipe
bcrypt = Bcrypt(app)

@app.route('/')
def main():
    return render_template('index.html')

#-------------------------------
# The register form
#-------------------------------
@app.route('/register', methods=['POST'])
def add_user():
    
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : request.form['password'],
        "conf_pass" : request.form['conf_pass']
    }
    if not User.user_valid(data):
        return redirect('/')

    print(request.form["password"])
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)

    # update the password field of our data object to be the hashed password
    data["password"] = pw_hash

    add_user = User.create_user(data)
    session["user_id"] = add_user

    return redirect('/dashboard')


#---------------------------
# The Login Form 
#---------------------------
@app.route('/login', methods=['POST'])
def show_user():
    # collect data from the form
    data = {
        "email" : request.form['email'],
        "password" : request.form['password']
    }
    # validate form data
    if not User.login_validate(data):
        return redirect('/')
    # Log in user
    logged_user = User.get_by_email(data)

    session["user_id"] = logged_user.id

    return redirect('/dashboard')

#------------------------------
# Dashboard, logged in user
#------------------------------
@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        flash("Please login or register before entering the site!")
        return redirect('/')

    data = {
        "user_id" : session['user_id']
    }

    user = User.get_by_id(data)
    all_recipe = Recipe.get_all()

    return render_template('dashboard.html', all_recipe = all_recipe, user = user)

#-------------------------
# Logout of user account
#-------------------------

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")