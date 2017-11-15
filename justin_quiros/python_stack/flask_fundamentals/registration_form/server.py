# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['GET', 'POST'])
def process():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif len(request.form['first_name']) < 1:
    	flash("Please enter your first name.")
    elif len(request.form['last_name']) < 1:
		flash("Please enter your last name.")
    elif len(request.form['password']) < 1:
		flash("Please enter a password.")
    elif len(request.form['password']) < 8:
    	flash("Your password must be more than 8 characters")
    elif len(request.form['confirm_password']) < 1:
		flash("Please confirm the password.")
    elif len(request.form['confirm_password']) < 8:
    	flash("Your password must be more than 8 characters")
    elif request.form['password'] != request.form['confirm_password']:
		flash("The password you have entered does not match.")
    return	redirect('/')

app.run(debug=True)
