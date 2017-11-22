from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "thisMustBeTrumpsWallCuzItSucks"
mysql = MySQLConnector(app, 'wall')

@app.route('/', methods=['get'])
def index():
	return render_template('index.html')
	if id not in session:
		session['id'] = id

@app.route('/register', methods = ['post'])
def register():
	valid = True
	newData = {
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
		flash("First name must be greater than 2 characters")
		valid = False
	elif not first_name.isalpha():
		flash("First name must contain only letters")
		valid = False

	if last_name < 0:
		flash("Last name must be greater than 2 characters")
		valid = False
	elif not last_name.isalpha():
		flash("Last name must contain only letters")
		valid = False

	if len(email) < 0 or len(password) < 0 or len(cPassword) < 0 :
		flash("Email and password required")
		valid = False
	elif len(password) < 8:
		flash("Password too short must be 8 characters")
		valid = False
	elif password != cPassword:
		flash("Passwords dont match")
		valid = False
	elif not EMAIL_REGEX.match(email):
		flash("Not a valid email")
		valid = False

	if valid:
		query = "SELECT email FROM users WHERE email = :email"
		emails = mysql.query_db(query, {'email':email})
		if emails:
			flash("Email already taken")
		else:
			query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())" 
			session['user_id'] = mysql.query_db(query, newData)
			print session['user_id']
			print "registered!"
			return redirect('/wall')

	return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
	valid = True
	userData = {
		'user_email': request.form['user_email'],
		'user_password': request.form['user_password'],
	}
	if request.form['user_email'] < 2 :
		valid = False
		flash("Invalid Email")
	elif request.form['user_password'] < 2:
		valid = False
		flash("Invalid Password")
	if valid:
		query = "SELECT * FROM users WHERE email = :email"
		users = mysql.query_db(query, {'email':userData['user_email']})
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
	session.pop('user_id')
	return redirect('/')

@app.route('/wall')
def wall():
	if 'user_id' not in session:
		return redirect('/')

	query = "SELECT messages.id, messages.message, users.first_name AS user FROM messages JOIN users on users.id = messages.user_id ORDER BY 'created_at' DESC"
	messages = mysql.query_db(query)

	query = "SELECT comments.id, comment, message_id, first_name AS user FROM comments JOIN users on users.id = comments.user_id ORDER BY 'created_at' DESC"
	comments = mysql.query_db(query)

	mysql.query_db(query)
	return render_template('wall.html', messages=messages, comments=comments)

@app.route('/messages', methods=["post"])
def newMessage():
	message = request.form['message']
	if message =="":
		return redirect('/wall')

	query = "INSERT INTO messages (message, user_id, created_at) VALUES (:message, :user_id, NOW())"
	data = {'message':message, 'user_id': session['user_id']}

	mysql.query_db(query, data)
	return redirect('/wall')

@app.route('/comments', methods=["post"])
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
