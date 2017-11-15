from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random

#sets the a random number between 1 and 100 to the session number 
@app.route('/')
def welcome():
	result =""
	if 'number' not in session:
		session['number'] = random.randrange(0, 101)

	if 'guess' not in session:
		session['guess'] = 0

	if session['guess'] == session['number']:
		result = "Correct"
	elif session['guess'] > session['number']:
		result = "to high"
	elif session['guess'] < session['number']:
		result = "to low"

	# print session['number']
	return render_template('index.html', result=result)

@app.route('/guess', methods=['POST'])
def guess():

	session['guess'] = int(request.form['guess'])
	# if session['guess'] == session['number']:
	# 	result = 'You win!!!'
	# elif request.form['guess'] > session['number']:
	# 	result = 'To high'
	# elif request.form['guess'] < session['number']:
	# 	result = 'To low'
	# print session['guess']
	#print guess
	# print int(request.form['guess'])
	return redirect('/')


#clears the session
@app.route('/again', methods=['POST'])
def again():
	session.clear()
	return redirect('/')

app.run(debug=True)