from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
import re
import md5
import os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'login_registration')
# an example of running a query
# print mysql.query_db("SELECT * FROM email_addresses")
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():




	query = "SELECT * FROM users"                           # define your query
	users = mysql.query_db(query)                           # run query with query_db()
	return render_template('index.html', all_users= users) # pass data to our template



@app.route('/login', methods=["POST"])
def login():
	error = 0

	login_password = md5.new(request.form['password']).hexdigest()
	login_email = request.form['email']
	session['logged_on'] = ""

	if len(login_email) < 1:
		flash("Email cannot be blank!")
		error = 1
	elif not EMAIL_REGEX.match(login_email):
		flash("Invalid Email Address!")
		error = 1
	else:
		user_query = "SELECT password, id FROM users where users.email = :email"
		query_data = { 'email': login_email}
		user = mysql.query_db(user_query, query_data)
		print user
		if user == []:
			flash("Email address is not registered")
			error = 1
		else:
			db_pwd = user[0]['password']
			if db_pwd != login_password:
				flash("Invalid password")
				error = 1
			else:
				session['logged_on'] = user[0]['id']
				print session['logged_on']
			if error == 0:
				return render_template('/success.html')
			else:
				return redirect('/')




@app.route('/register', methods=["POST"])
def register():
	error = 0
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

		hashed_password = md5.new(request.form['password']).hexdigest()

		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

		data = {
				'first_name': request.form['first_name'],
				'last_name': request.form['last_name'],
				'email': request.form['email'],
				'password': hashed_password
		}

		mysql.query_db(query, data)

		return redirect('/')
	else:
		return redirect('/')


app.run(debug=True)


