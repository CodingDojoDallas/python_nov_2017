from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SecretKey"
mysql = MySQLConnector(app,'walldb') #name of database schema

import md5
import os, binascii

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users = users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/wall')
def wall():
    #NOBODY LOGGED IN
    if session.get('userid') == None:
        return redirect('/')
    
    user_query = "SELECT first_name, last_name FROM users WHERE users.id = :id"
    user_data = {'id': session['userid']}
    user = mysql.query_db(user_query, user_data)

    messages_query = "SELECT users.id, messages.id, first_name, last_name, message, messages.created_at FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(messages_query)

    comments_query = "SELECT messages.id AS message_id, comments.id AS comment_id, first_name, last_name, comment, comments.created_at FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id ORDER BY comments.created_at DESC"
    comments = mysql.query_db(comments_query)

    return render_template('wall.html', 
        first_name = user[0]['first_name'],
        all_messages = messages,
        all_comments = comments)

@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
        'user_id': session['userid'],
        'message': message
        }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    comment = request.form['comment']
    message_id = request.form['message_id']
    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    data = {
        'user_id': session['userid'],
        'message_id': message_id,
        'comment': comment
        }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/register', methods=['POST'])
def register():
    errors = False

    #CHECK VALID FIRST/LAST NAME
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if first_name.isalpha() == False or last_name.isalpha() == False:
        flash("First/Last name can only be letters")
        errors = True
    if len(first_name) < 2 or len(last_name) < 2:
        flash("First/Last name needs to be at least 2 characters")
        errors = True

    #CHECK IF EMAIL HAS CORRECT FORMAT
    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        errors = True

    #CHECK IF EMAIL ALREADY IN DATABASE
    user_query = "SELECT email FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    email_check = mysql.query_db(user_query, query_data)
    if len(email_check) != 0:
        flash("Email already exists!")
        errors = True

    #CHECK PASSWORDS
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
    else: #Successful Registration
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
        flash("Registration Successful! You can log in now :)")
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['hashed_pw'] == encrypted_password: #successful login
            session['userid'] = user[0]['id']
            print session['userid']
            return redirect('/wall')
        else: #invalid password!
            flash("Invalid login password!")
            return redirect('/')
    else: #invalid email!
        flash("Invalid login email")
        return redirect('/')

app.run(debug=True)

    
        