from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, redirect, request

from user import User   # importing class from user.py
app = Flask(__name__)

@app.route('/')
def index():
    users = User.users_info()
    print(users)
    return render_template('index.html', users = users)

# -------------------------------------------
# Add new user
#--------------------------------------------
@app.route('/new_user')
def new_user(): 
    return render_template('new.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    # packing info into data to send to query
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    # call on query
    new_user = User.insert_users(data)
    return redirect('/')

# -------------------------------------------
# Show user data individually
#--------------------------------------------
@app.route('/<int:user_id>')
def show_user(user_id):
    data = {
        "user_id" : user_id
    }
    display = User.display_user(data)
    print(display)
    display.created_at = display.created_at.strftime("%B %d %Y")
    if display.updated_at != None:
        display.updated_at = display.updated_at.strftime("%B %d %Y")
    return render_template('read_user.html', display = display)

# -------------------------------------------
# Edit and update users
#--------------------------------------------
@app.route('/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        "user_id" : user_id
    }
    # call on query
    user = User.display_user(data)
    return render_template('edit_user.html', user = user)

@app.route('/update_user/<int:user_id>', methods=["POST"])
def update_user(user_id):
    data = {
        'user_id' : user_id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }

    updated_user = User.update_user(data)
    return redirect('/')

# -------------------------------------------
# Delete User
#--------------------------------------------
@app.route('/<user_id>/delete')
def delete(user_id):
    data = {
        "user_id" : user_id
    }
    # Call on query
    delete_user = User.delete_user(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True) 