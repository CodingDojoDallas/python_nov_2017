from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SecretKey"
mysql = MySQLConnector(app,'usersdb') #name of database schema

import md5
import os, binascii

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users = users)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/register', methods=['POST'])
def register():
    errors = False

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if first_name.isalpha() == False or last_name.isalpha() == False:
        flash("First/Last name can only be letters")
        errors = True
    if len(first_name) < 2 or len(last_name) < 2:
        flash("First/Last name needs to be at least 2 characters")
        errors = True

    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        errors = True

    password = request.form['password']
    if len(password) < 8:
        flash("Password needs to be at least 8 characters")
        errors = True

    password_confirm = request.form['password_confirm']
    if password_confirm != password:
        flash("Confirmed Password doesn't match!")
        errors = True

    if errors == True:
        return redirect('/')
    else:
        salt =  binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, hashed_pw, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW(), NOW())"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'hashed_pw': hashed_pw,
            'salt': salt
            }
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['hashed_pw'] == encrypted_password:
            # successful login
            return redirect('/success')
        else:
            # invalid password!
            flash("Invalid login email / password!")
            return redirect('/')
    else:
        # invalid email!
        flash("Invalid login email / password!")
        return redirect('/')

app.run(debug=True)