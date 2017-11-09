from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email_db')
# an example of running a query
# print mysql.query_db("SELECT * FROM email_addresses")
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():




	query = "SELECT * FROM email_addresses"                           # define your query
	email_addresses = mysql.query_db(query)                           # run query with query_db()
	return render_template('index.html', all_emails=email_addresses) # pass data to our template


	
	# friends = mysql.query_db("SELECT * FROM friends")
	# print friends
	# return render_template('index.html') # pass data to our template


@app.route('/process', methods=["POST"])
def process():
	error = 0

	email = request.form['email']
	session['email'] = email

	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
		error = 1
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
		error = 1
	else:
		query = "SELECT * FROM email_addresses WHERE address = '" + email + "'"
		exist = mysql.query_db(query)

		if exist != []:
			error = 1
			flash("Email already exists")

	if error == 0:
		query = "INSERT INTO email_addresses (address, created_at) VALUES (:address, NOW())"

		data = {
				'address': request.form['email']
		}

		mysql.query_db(query, data)
		return redirect('/success')
	else:
		return redirect('/')


@app.route('/success')
def success():
	query = "SELECT * FROM email_addresses"
	email_list = mysql.query_db(query)
	return render_template('success.html', email = session['email'], all_emails= email_list)

app.run(debug=True)


