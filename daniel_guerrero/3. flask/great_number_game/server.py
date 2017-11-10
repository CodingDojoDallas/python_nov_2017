from flask import Flask, render_template, redirect, session, flash, request
import random

app = Flask(__name__)

app.secret_key = 'Patriots_Suck'



@app.route('/')
def index():

	if 'num' not in session:
		session['num'] = random.randint(1, 101)

	if 'Correct' not in session:
		session['Correct'] = False


	print session['num']
	print session['Correct']

	return render_template('index.html')


@app.route('/guessed', methods=['POST'])
def guess():

	if int(request.form['number']) == session['num']:
		session['Correct'] = True
		flash("You guessed it!")
	
		return redirect('/')

	elif int(request.form['number']) < session['num']:
		flash('Your Number Is Too Low!')
		return redirect('/')
	else:
		flash('Your number is too high')

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	print "woohoo"
	session.clear()

	return redirect('/')



app.run(debug=True)