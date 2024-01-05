from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def homepage():
    return render_template('homepage.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

app.run()