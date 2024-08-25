from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sobre")
def bye():
    return "Hello, World!"


if __name__=='__main__':
    app.run(debug=True)