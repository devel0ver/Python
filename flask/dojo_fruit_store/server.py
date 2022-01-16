from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = '4664126914tr73'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['id'] = request.form['student_id']
    session['count_s']= int(request.form['strawberry'])
    session['count_a']= int(request.form['apple'])
    session['count_r']= int(request.form['raspberry'])
    total = session['count_a'] + session['count_r'] + session['count_s'] 
    print(f"Charging {request.form['first_name']} for {total} fruits")
    return redirect('/display')

@app.route('/display')
def display_user():
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    