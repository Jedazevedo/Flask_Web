from flask import Flask, request, render_template, session, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


@app.route("/sobre")
def sobre():
    return "TELA SOBRE SO NOSSO APP!"
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

#static files  
    
if __name__=='__main__':
    app.run(debug=True) 
# venv ativado
# debug ativado sozinho, use o comando: flask --app hello.py run --debug