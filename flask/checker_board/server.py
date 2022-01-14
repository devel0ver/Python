from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template("index.html", rows=8, col=8)

@app.route('/<int:col>/<string:color>/<string:color2>')
def count(col, color, color2):
    return render_template("index.html", col=col, rows=8, color = color, color2=color2)

@app.route('/<int:rows>/<int:col>')
def colors(rows, col):
    return render_template("index.html", rows = rows, col = col)


if __name__ == "__main__":
    app.run(debug=True)