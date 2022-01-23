from flask_app.models.dojo import Dojo
from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.ninja import Ninja


@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', dojos = dojos)

#--------------------------------------
# Add a new dojo 
#--------------------------------------
@app.route('/dojos/add_dojo', methods=['POST'])
def add_dojo():
    data = {
        'name' : request.form['name']
    }
    add_dojo = Dojo.save(data)
    return redirect('/dojos')

#--------------------------------------
# Show all the ninjas in dojo
#--------------------------------------
@app.route('/dojos/<int:dojo_id>')
def show_info(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    show_one_dojo = Dojo.show_one_dojo(data)
    print(show_one_dojo)
    return render_template('show_info.html', dojo = show_one_dojo)

#--------------------------------------
# Add new ninja to dojo
#--------------------------------------
@app.route('/add_ninja')
def add_ninja():
    holder = Dojo.get_all()
    return render_template('add_ninja.html', holder = holder)

@app.route('/new_ninja', methods=['POST'])
def new_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    add_ninja = Dojo.add_ninja(data)
    return redirect('/dojos')


