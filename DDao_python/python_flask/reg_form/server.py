from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecretKey!" 

@app.route('/')
def index():
	
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

	session['fname'] = request.form['fname']
	session['lname'] = request.form['lname']
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['cpwd'] = request.form['cpwd']


	if len(request.form['email']) == 0:
		flash("Email cannot be empty!")
	elif not EMAIL_REGEX.match(session['email']):
		flash("Invalid Email!")

	if len(request.form['fname']) == 0:
		flash("Name cannot be empty!")
	elif re.search(r'[0-9]', session['fname']):
		flash("First name cannot contain numbers!")

	if len(request.form['lname']) == 0:
		flash("Last name cannot be empty!")
	elif re.search(r'[0-9]', session['lname']):
		flash("Last name cannot contain numbers!")

	if len(request.form['password']) == 0:
		flash("Enter password!")
	elif len(request.form['password']) < 8:
		flash("Password must contain at least 8 characters!")

	if len(request.form['cpwd']) == 0:
		flash("Confirm your Password!")
	elif session['password'] != session['cpwd']:
		flash("Passwords do not match")
	else:
		flash('Thanks for submitting your information.')

	return redirect('/')

app.run(debug=True)