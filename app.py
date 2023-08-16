from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

app.config['MYSQL_HOST']=os.getenv('MYSQL_HOST')
app.config['MYSQL_USER']=os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD']=os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB']=os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)