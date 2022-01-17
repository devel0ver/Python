from markupsafe import re
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = '89572095tt42'

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def info():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['gender'] = request.form['sex']
    if session['comments'] == '' and session['gender'] == 'Male':
        print(f"Gender: {session['gender']}, his name is {session['name']}, he lives in {session['location']}, and he loves {session['language']}.\n( {session['name']}'s comments: There are no comments )")
    elif session['comments'] == '' and session['gender'] == 'Female':
        print(f"Gender: {session['gender']}, her name is {session['name']}, she lives in {session['location']}, and she loves {session['language']}.\n( {session['name']}'s comments: There are no comments )")
    elif session['gender'] == 'Male':
        print(f"Gender: {session['gender']}, his name is {session['name']}, he lives in {session['location']}, and he loves {session['language']}.\n( {session['name']}'s comments: {session['comments']} )")
    else:
        print(f"Gender: {session['gender']}, her name is {session['name']}, she lives in {session['location']}, and she loves {session['language']}.\n( {session['name']}'s comments: {session['comments']} )")
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)