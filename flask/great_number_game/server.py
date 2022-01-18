from crypt import methods
from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = '31902r8h0'

@app.route('/') 
def index():
    if 'rand_guess' not in session: 
        session['rand_guess'] = int(random.randint(1,100))
        session['num_of_guesses'] = 0
    print(f"Computer Guess: {session['rand_guess']}")
    count = session['num_of_guesses']
    user = None
    location = None

    if 'user_guess' in session:
        location = session['location']

    return render_template('index.html', count=count, location=location)

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['num'])
    session['user_guess'] = user_guess

    rand = int(session['rand_guess']) 
    session['num_of_guesses'] = int(session['num_of_guesses']) + 1   # increment the number of gueses by 1

    if user_guess > rand:
        print(f"User Guess: {user_guess}\nToo HIGH")
        session['location'] = 'HIGH'

    if user_guess < rand:
        print(f"User Guess: {user_guess}\nToo LOW")
        session['location'] = 'LOW'
    
    if user_guess == rand:
        print(f"User Guess: {user_guess}\nJackPot!!")
        session['location'] = 'correct'
    
    # if session['num_of_guesses'] > 5:
    #     session.clear()

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/leaderboard', methods=['POST'])
def leaderboard():
    attempt = session['num_of_guesses']
    request.form['name']
    user_name = [
        {"Name" : request.form['name']}
    ]
    user_name.append({"Name" : request.form['name']})
    print(f"{user_name} {attempt}")
    return render_template('leaderboard.html', user_name=user_name, attempt=attempt)

if __name__ == '__main__':
    app.run(debug=True)


