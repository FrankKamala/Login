from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "kamala"

@app.route("/user")
def log():
    return render_template('login.html')

 

    

