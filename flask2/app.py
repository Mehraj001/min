import re
from flask import Flask, config ,render_template,request,redirect
import os
from flask_sqlalchemy import SQLAlchemy
import json
from werkzeug.utils import secure_filename
from flask_mail import Mail
from random import randint
app = Flask(__name__)
with open("config.json","r") as c:
    params=json.load(c)["params"]
mail=Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER']=params["UPLOAD_LOCATION"]
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avtar=  db.Column(db.String(120), unique=True, nullable=False)
    pasw=  db.Column(db.String(120), nullable=False)
@app.route("/check",methods=['GET','POST'])
def check():
    if request.method=='POST':
        name=request.form.get("check")
        print(name) 
    return render_template("hht.html")
@app.route("/see/<string:x>",methods=['GET','POST'])
def see(x):
    return render_template("det.html")
@app.route("/log",methods=['GET','POST'])
def log():
    return render_template("log.html")
@app.route("/sing",methods=['GET','POST'])
def sing():
    return render_template("sign.html")
@app.route("/sign",methods=['GET','POST'])
def sign():
    
    if request.method=='POST':
        # name=request.form.get('user')
        passw=request.form.get('passw')
        email=request.form.get('email')
        x=randint(100,1000000000)
        # f=request.files['file']
        # f.filename=name+'.jpg'
        # x=f.filename
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        enter=User(username=email,email=email,avtar=str(x),pasw=passw)
        db.session.add(enter)
        db.session.commit()
    return redirect("index.html")
@app.route("/")
def hello_world():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)