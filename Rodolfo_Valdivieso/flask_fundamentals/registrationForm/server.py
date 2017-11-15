from flask import Flask, render_template, request, redirect, flash
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'

@app.route('/')              
def index():
	return render_template('index.html')      

@app.route('/process', methods=['POST'])
def processF():

	firstName = request.form['firstName']
	lastName = request.form['lastName']
	email = request.form['email']
	birthday = request.form['birthday']
	password = request.form['password']
	password2 = request.form['password2']
	error = 0
	if len(firstName) < 1 :
		flash("Name cannot be empty!")
		error = 1
	elif any(map(str.isdigit, str(firstName))):
		flash('First Name cannot contain Numbers.')
		error = 1
	if len(lastName) < 1 :
		flash("Last Name cannot be empty!")
		error = 1
	elif any(map(str.isdigit, str(lastName))):
		flash('Last Name cannot contain Numbers.')
		error = 1
	if len(email) < 1 :
		flash("Email cannot be empty!")
		error = 1
	elif not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!")
	
	if birthday=="":
		flash("Birthdate cannot be empty!")
		error = 1

	try:
		datetime.datetime.strptime(str(birthday), '%m/%d/%Y')
	except ValueError:
		flash("Invalid birthdate format!")
		error=1

	if len(password) < 8:
		flash("Password must be at least 8 char long!")
		error = 1
	elif not any(map(str.isupper, str(password))):
		flash('Your password needs at least 1 capital.')
		error = 1
	elif not any(map(str.isdigit, str(password))):
		flash('Your password needs at least 1 number.')
		error = 1
	elif password != password2:
		flash("Password is not equal to Confirm Password!")
		error = 1

	return render_template('index.html', firstName=firstName, lastName=lastName, email=email, birthday=birthday, password=password, password2=password2, error=error)
	

@app.route('/reset', methods=['POST'])              
def goback():
	return redirect('/')

app.run(debug=True)      # Run the app in debug mode.