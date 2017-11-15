from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'email')

@app.route('/')
def home():
	query = "SELECT * FROM email"
	email = mysql.query_db(query)
	print email
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	if len(request.form['email']) < 1 or EMAIL_REGEX.match(request.form['email']):
		flash("Email not valid!", "fail")
	else:
		query = "SELECT * FROM email"
		email = mysql.query_db(query)
		# print email
		flash("The email address you entered is a VALID email address! Thank you!", "success")
		query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"
    # We'll then create a dictionary of data from the POST data received.
		data = {
			'email': request.form['email']
			}
    # Run query, with dictionary values injected into the query.
		mysql.query_db(query, data)
		return render_template("success.html", email = email)
	return redirect('/')

app.run(debug=True)