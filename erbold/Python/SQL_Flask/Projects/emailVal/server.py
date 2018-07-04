from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re


app = Flask(__name__)
mysql = MySQLConnector(app,'emailval')
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = 'yank'


@app.route('/')
def index():

	return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():
    # add a friend to the database!
	session['email'] = request.form['email']
	print session['email']
	if not emailRegex.match(session['email']):
		flash("Invalid Email Address!")	
		return redirect('/')

	else:
		flash("Valid Email Address")
		query = "INSERT INTO emails (email, created_at, updated_at)VALUES(:email, NOW(), NOW())"
		data = {
			'email': request.form['email']
		}
		mysql.query_db(query, data)
		return redirect('/success')

@app.route('/success')
def show_emails():
	email = session['email']
	query = "SELECT email, date_format(created_at, '%m:%d:%y %1:%i %p') as created_at FROM emails"
	emails = mysql.query_db(query)

	return render_template('success.html', emails = emails, email = email)

app.run(debug=True)