import md5, os, binascii, random
from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "nukedMyFirstTry"
mysql = MySQLConnector(app,'logNreg')


@app.route('/')
def index():
    return render_template('index.html')
    if id not in session:
        session['id'] = id

@app.route('/register', methods = ['POST'])
def reg():
    valid = True
    newUser = {
        'email': request.form['email'],
        'hashPass': request.form['hashPass'],
        'cPassword': request.form['cPassword'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    email = request.form['email']
    hashPass = request.form['hashPass']
    cPassword = request.form['cPassword']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    if first_name < 2:
        flash("name must be greater than 2 characters")
        valid = False
    elif not first_name.isalpha():
        flash("name must be letters only")
        valid = False        

    if last_name < 2:
        flash("name must be greater than 2 characters")
        valid = False
    elif not last_name.isalpha():
        flash("name must be letters only")
        valid = False
    
    if len(email) < 1 or len(hashPass) < 1 or len(cPassword) < 1 :
        flash("email and hashPass required")
        valid = False
    elif len(hashPass) < 8:
        flash("hashPass is too short")
        valid = False
    elif hashPass != cPassword:
        flash("passwords dont match")
        valid = False
    elif not EMAIL_REGEX.match(email):
        flash("email not valid")
        valid = False

    if valid:    
        query = "SELECT email FROM users WHERE email = :email"
        emails = mysql.query_db(query, {'email':email})
        if emails:
            flash("email already in use")
        else:
            newUser['salt'] = binascii.b2a_hex(os.urandom(15))
            newUser['hash'] = md5.new(request.form['hashPass']+newUser['salt']).hexdigest()
            query = "INSERT INTO users (first_name, last_name, email, hashPass, salt, created_at, updated_at) Values ( :first_name, :last_name, :email, :hashPass, :salt, NOW(), NOW() )" 
            session['user_id'] = mysql.query_db(query, newUser)
            print session['user_id']
            print "You registered!"
            return redirect('/success')

    return redirect('/')
@app.route('/login', methods = ['POST'])
def login():
    valid = True
    newUser = {
        'user_email': request.form['user_email'],
        'user_password': request.form['user_password'],
    }
    if request.form['user_email'] < 2 :
        valid = False
        flash("fail")
    elif request.form['user_password'] < 2:
        valid = False
        flash("wrong")
    if valid:
        query = "SELECT * FROM users WHERE email = :email"
        users = mysql.query_db(query, {'email':newUser['user_email']})
        if len(users) > 0:
            user = users[0]
            if md5.new(request.form['user_password']+user['salt']).hexdigest():
                flash("You are logged in")
                session['user_id'] = user['id']
                return redirect('/success')
            else:
                flash("Login failed")
                return redirect ('/')
        else:
            flash("User not found")
            return redirect ('/')

@app.route('/success')
def show():
    query = "SELECT * from users WHERE id = :id"
    data = {'id' :session['user_id']}
    users = mysql.query_db(query, data)
    print data
    return render_template('show.html', user = users[0])



app.run(debug=True)

