from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Handles requests to the root URL and returns a simple greeting.
    """
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
