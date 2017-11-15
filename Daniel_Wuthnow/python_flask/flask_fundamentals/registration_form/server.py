from flask import Flask, render_template, request, redirect, session, flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'log_reg_db')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	if len(request.form['email']) < 1:
		flash("You need to have an email", "email")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email Address!', "email")

	if len(request.form['first_name']) < 1:
		flash("We need a first name", "first")
	elif request.form['first_name'].isalpha() == False:
		flash("Names dont have numbers", "first")

	if len(request.form['first_name']) < 1:
		flash("We need a last name", "last")
	elif request.form['first_name'].isalpha() == False:
		flash("Names dont have numbers", "last")

	if len(request.form['password']) < 1:
		flash("We need a password", "password")
	elif len(request.form['password']) < 8:
		flash("password is not long enough", "password")

	if request.form['password_comp'] != request.form['password']:
		flash("password dose not match", "password_comp")
	return redirect('/')


app.run(debug=True)