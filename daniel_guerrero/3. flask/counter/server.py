from flask import Flask, render_template, redirect, session, flash

app = Flask(__name__)

app.secret_key = 'Patriots_Suck'


@app.route('/')
def index():

# Checking for a Session "counter" if none set it to 1
	if session.get('counter') == None:

		counter = 1

# Session "counter" is being declared
		session['counter'] = counter

	return	render_template('index.html')



@app.route('/add')
def add():

	session['counter'] += 2
	return redirect('/')




@app.route('/clear')
def remove():

	session['counter'] = 1
	return redirect('/')


app.run(debug=True)