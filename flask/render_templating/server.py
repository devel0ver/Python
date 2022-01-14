from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="Hello", times=5)

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<string:sent>/<int:num>')
def hello(sent,num):
    return render_template("hello.html",sent=sent,num=num)

if __name__ == "__main__":
    app.run(debug = True)