from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv
from sqlhelpers import *
from forms import *

load_dotenv()

app=Flask(__name__)

app.config['MYSQL_HOST']=os.getenv('MYSQL_HOST')
app.config['MYSQL_USER']=os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD']=os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB']=os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS']='DictCursor'
 

mysql= MySQL(app)

def log_in_user(username):
    users= Table("users","name","email","username","password")
    user= users.getone("username",username)

    session['logged_in']=True
    session['username']=username
    session['name']=user.get('name')
    session['email']=user.get('email')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm(request.form)
    users=Table("users","name","email","username","password")

    if request.method == 'POST' and form.validate():
        username= form.username.data
        email= form.email.data
        name= form.name.data   

        if isnewuser(username): #Check if is new user
            password= sha256_crypt.encrypt(form.password.data)
            users.insert(name,email,username,password)
            log_in_user(username)
            return redirect(url_for('dashboard'))
        else:
            flash('User already exists','danger')
            return redirect(url_for('register'))

    return render_template("register.html",form=form)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html',session=session)




@app.route('/')
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)