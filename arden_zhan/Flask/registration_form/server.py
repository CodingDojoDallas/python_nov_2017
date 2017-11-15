from flask import Flask, render_template, request, redirect, session, flash

import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def result():

    email = request.form['email']
    first_name = request.form['first_name'] 
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    errors = False

    if len(email) < 1:
        flash("Email cannot be empty!")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        errors = True
        
    if len(first_name) < 1:
        flash("First name cannot be empty")
        errors = True
        
    if len(last_name) < 1:
        flash("Last name cannot be empty")
        errors = True

    if len(password) < 1:
        flash("Password cannot be empty")
        errors = True

    if confirm_password != password:
        flash("Confirmed password does not match")
        errors = True

    if errors == False:
        flash("Thanks for submitting your information.")
    return redirect('/')

app.run(debug = True)
