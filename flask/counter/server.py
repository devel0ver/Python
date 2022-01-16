from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "13142345"

@app.route('/')
def visits():
    if 'num' in session:
        session['num'] = session['num']+1
    else:
        session['num'] = 1
    return render_template('index.html')

@app.route('/', methods=['POST'])
def two_visits():
    session['num'] = session['num'] + 1
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)