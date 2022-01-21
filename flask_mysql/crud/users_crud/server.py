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

if __name__ == '__main__':
    app.run(debug = True) 