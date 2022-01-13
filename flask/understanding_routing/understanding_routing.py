from flask import Flask     # Import Flask to allow us to create our app
app = Flask(__name__)       # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hello_name(name):
    print(name)
    return f"Hi {str(name)}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    print(word)
    print(num)
    return int(num)*str(word)

if __name__ == "__main__":      # Ensure this file is being run directly and not from a different module
    app.run(debug=True)         # Run the app in debug mode.
