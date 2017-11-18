from flask import Flask, flash, render_template, request, redirect, session
import re

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
app.secret_key = 'dope'

def countLetters(word):
    count = 0
    for c in word:
        count += 1
    return count

@app.route("/")
def index():

    # if session.get('num') == None:
    #     setSession()
    # else:
    #     pass
    # print session['num']	
    return render_template("index.html")


@app.route("/answer", methods = ['POST'])
def result():
	First_name = request.form['fname']
	Last_name = request.form['lname']
	Email = request.form['email']
	Password = request.form['password']
	Conf_Password = request.form['password2']
	
	if First_name == '' or Last_name == '' or Email == '' or Password == ''or Conf_Password == '':
		flash('error blank', 'error')
		return redirect('/')

	if any(char.isdigit() for char in Last_name) == True or any(char.isdigit() for char in First_name) == True:
		flash('Name cant have numbers', 'error') 
		return redirect('/')

	session['password'] = request.form['password']
	password = countLetters(session['password'])
	print password
	if password < 9:
		flash('length error', 'error')
		return redirect('/')

	if not emailRegex.match(Email):
		flash("Invalid Email Address!", 'error')	
		return redirect('/')

	if Password != Conf_Password:
		flash('Password does not match', 'error')	
		return redirect('/')

	return render_template("answer.html", First_name = First_name, Last_name = Last_name, Email = Email, Password = Password, Conf_Password = Conf_Password)
	return redirect('/')

app.run(debug=True)
