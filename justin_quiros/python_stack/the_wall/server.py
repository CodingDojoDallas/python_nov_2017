from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
import re
import md5
import os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'the_wall')
# an example of running a query
# print mysql.query_db("SELECT * FROM email_addresses")
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():




	query = "SELECT * FROM users"                           # define your query
	users = mysql.query_db(query)                           # run query with query_db()
	return render_template('index.html', all_users= users) # pass data to our template



@app.route('/login', methods=["GET", "POST"])
def login():
	error = 0

	password = request.form['password']
	login_email = request.form['email']
	session['logged_on'] = ""
	session['email'] = ""
	session['name'] = ""

	if len(login_email) < 1:
		flash("Email cannot be blank!")
		error = 1

		print login_email

	elif not EMAIL_REGEX.match(login_email):
		flash("Invalid Email Address!")
		error = 1
	else:
		user_query = "SELECT password, id, salt, first_name, last_name FROM users where users.email = :email"
		query_data = { 'email': login_email}
		user = mysql.query_db(user_query, query_data)
		print user
		if user == []:
			flash("Email address is not registered")
			error = 1
		else:
			db_pwd = md5.new(password + user[0]['salt']).hexdigest()
			if db_pwd != user[0]['password']:
				flash("Invalid password")
				error = 1
			else:
				session['logged_on'] = user[0]['id']
				print session['logged_on']
			if error == 0:
				session['first_name'] = user[0]['first_name']
				session['last_name'] = user[0]['last_name']
				session['email'] = login_email
				session['id'] = user[0]['id']
				return redirect('/wall')
			else:
				return redirect('/')


@app.route('/register', methods=["POST"])
def register():
	error = 0
	salt = '721'
	first_name = str(request.form['first_name'])
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	conf_password = request.form['conf_password']

	if len(request.form['first_name']) < 2:
		flash("First name must be atleast 2 letters")
		error = 1
	elif any(x.isdigit() for x in first_name):
		flash("Your first name can not have numbers")
		error = 1
	elif len(request.form['last_name']) < 2:
		flash("Last name must be atleast 2 letters")
		error = 1
	elif any(y.isdigit() for y in last_name):
		flash("Your last name can not have numbers")
		error = 1
	elif len(request.form['email']) < 1:
		flash("Email cannot be blank!")
		error = 1
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
		error = 1
	elif len(request.form['password']) < 8:
		flash("Password must be atleast 8 characters")
		error = 1
	elif password != conf_password:
		flash("The passwords provided are not the same")
		error = 1
	else:
		query = "SELECT * FROM users WHERE email = '" + email + "'"
		exist = mysql.query_db(query)

		if exist != []:
			error = 1
			flash("This email is already registered")

	if error == 0:

		hashed_password = md5.new(password + salt).hexdigest()

		query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"

		data = {
				'first_name': request.form['first_name'],
				'last_name': request.form['last_name'],
				'email': request.form['email'],
				'password': hashed_password,
				'salt': salt
		}

		mysql.query_db(query, data)

		return redirect('/')
	else:
		return redirect('/')







@app.route('/post_mess', methods=["GET", "POST"])
def post_mess():


	user_query = "SELECT id, first_name, last_name FROM users where users.email = :email"
	query_data = { 'email': session['email']}
	user = mysql.query_db(user_query, query_data)
	print user

	

	query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"

	data = {
			'user_id': user[0]['id'],
			'message': request.form['message']
	}

	mysql.query_db(query, data)
	print "we made it"
	return redirect('/wall')






@app.route('/comment', methods=["GET", "POST"])
def comment():

	query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"

	data = {
			'user_id': session['id'],
			'message_id': request.form['post_id'],
			'comment': request.form['comment']
	}

	mysql.query_db(query, data)
	print "we made it"
	return redirect('/wall')



@app.route('/wall', methods=["GET", "POST"])
def wall():
	query = """SELECT b.id as post_id, CONCAT(a.first_name,' ', a.last_name) AS post_name, date_format(b.created_at, '%M %D %Y') AS post_date, b.message, c.id as comment_id, date_format(c.created_at, '%M %D %Y') AS comment_date, CONCAT(d.first_name,' ', d.last_name) AS comment_name, c.comment
				FROM users a JOIN messages b ON a.id = b.user_id
				LEFT JOIN comments c ON b.id = c.message_id
				LEFT JOIN users d ON d.id = c.user_id ORDER BY post_id desc, comment_id desc"""                          # define your query
	messages = mysql.query_db(query)                           # run query with query_db()
	return render_template('wall.html', all_messages = messages) # pass data to our template

@app.route('/log_off', methods=['POST'])
def clear():
	session.clear()
	return redirect('/')


app.run(debug=True)


