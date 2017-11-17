from flask import Flask, render_template,redirect,request,session,flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'.*[0-9].*')
Upper_REGEX = re.compile(r'.*[A-Z].*')
app =Flask(__name__)
app.secret_key ="ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
	if len(request.form['email'])<1:
		flash("Email cannot be blank")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	elif len(request.form['first_name'])<1:
		flash("First Name cannot be empty")
	elif  re.search(r'[0-9]',request.form['first_name']):
		flash("First Name cannot contain any number")
	elif len(request.form['last_name'])<1:
		flash("Last Name cannot be empty")
	elif re.search(r'[0-9]' ,request.form['last_name']):
		flash("Last Name cannot contain any number")
	elif len(request.form['password'])<1:
		flash("Password cannot be empty")
	elif len(request.form['password'])<8 and len(request.form['confrim'])<8:
		flash("Password should be more then 8 character")
	elif not PASSWORD_REGEX.match(request.form['password']):
		flash("Password Contain atleast 1 number ")	
	elif not Upper_REGEX.match(request.form['password']):
		flash("Password Contain atleast 1 Uppercase letter")
	elif len(request.form['confrim'])<1:
		flash("Password cannot be empty")
	elif request.form['password']!= request.form['confrim']:
		flash("Password not match try again!")
	elif len(request.form['date'])<1:
		flash("Birth Date cannot be empty")

	else:
		flash("Thank You Register Sucessfully !")

	return redirect('/')
app.run(debug=True)