from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "imBuildingThisWallForMeNotTRUMP!"

mysql = MySQLConnector(app, "wall")

@app.route('/', methods=['GET'])
def index():
    return render_template('root.html')
    if id not in session:
        session["id"] = id

@app.route('/register', methods=['POST'])
def register():
    error = True
    newUser = {
        'email': request.form['email'],
        'password': request.form['password'],
        'cPassword': request.form['cPassword'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    email = request.form['email']
    password = request.form['password']
    cPassword = request.form['cPassword']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    if first_name < 0:
        flash("First name field empty")
        error = False
    if last_name < 0:
        flash("Last name field empty")
        error = False
    if len(email) < 0 or len(password) < 0 or len(cPassword) < 0:
        flash("email and password is missing")
    elif len(password) < 8:
        flash("password not long enough")
        error = False
    elif password != cPassword:
        flash("passwords don't match")
        error = False
    elif EMAIL_REGEX.match(email):
        flash("Email not valid")
        error = False
    if error:
        query = "SELECT email FROM users WHERE email = :email"
        emails = mysql.query_db(query,{'email':email})
        if emails:
            flash("email not available")
        else:
            query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
            session ['user_id'] = mysql.query_db(Users)
            print session["user_id"]
            print "You're registered"
            return redirect('/wall')
    return redirect ('/')

@app.route('/login', methods = ['POST'])
def login():
    error = True
    newUser = {
        'user_email': request.form['user_email'],
        'user_password': request.form['user_password']
        }
    if request.form['user_email'] < 0:
        error = False
        flash("Invalid Email")
    if request.form['user_password'] < 0:
        error = False
        flash("Invalid Password")
    if error:
        query = "SELECT * FROM users WHERE email = :email"
        users = mysql.query_db(query, {'email':request.form['user_email']})
        if len(users) > 0:
            user = users[0]
            session['user_id'] = user['id']
            return redirect('/wall')
        else:
            flash("Login failed")
            return redirect ('/')
    else:
        flash("User not found")
        return redirect ('/')

@app.route('/logoff')
def logoff():
    session.pop ('user_id')
    return redirect ('/')

@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect ('/')
    query = "SELECT messages.id, messages.message, users.first_name, messages.created_at FROM messages JOIN users ON users.id= messages.users_id ORDER BY messages.created_at DESC"
    mysql.query_db(query)
    return render_template('wall.html')

@app.route('/messages', methods=["POST"])
def newMessage():
    message = request.form['message']
    if message =="":
        return redirect('/wall')
    query = "INSERT INTO messages (message, user_id, created_at) VALUES (:message, :user_id, NOW())"
    data = {'message':message, 'user_id': session['user_id']}
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comments', methods=["POST"])
def newComment():
    message_id = request.form['message_id']
    comment = request.form['comment']
    if comment =="":
        return redirect('/wall')
    query = "INSERT INTO comments (comment, created_at, message_id, user_id) VALUES (:comment, NOW(), :message_id, :user_id)"
    data = {'comment':comment, 'message_id':message_id, 'user_id': session['user_id']}
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)