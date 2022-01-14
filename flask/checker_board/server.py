from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template("index.html", col=8, rows=8, color="red", color2="black")

@app.route('/<int:rows>')
def columns(rows):
    return render_template("index.html", rows=rows, col=8, color = "red", color2="black")

@app.route('/<int:col>/<int:rows>')
def columns_rows(rows, col):
    return render_template("index.html", rows=rows, col=col, color = "red", color2="black")

@app.route('/<int:col>/<int:rows>/<string:color>/<string:color2>')
def colors(rows, col, color, color2):
    return render_template("index.html", rows = rows, col = col, color=color, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)