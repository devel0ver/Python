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
    if session['comments'] == "":
        print(f"The name is {session['name']}, lives in {session['location']}, loves {session['language']} language.\n( {session['name']} comments: There are no comments )")
    else:
        print(f"The name is {session['name']}, lives in {session['location']}, loves {session['language']} language.\n( {session['name']} comments: {session['comments']} )")
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)