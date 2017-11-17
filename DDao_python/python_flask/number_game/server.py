from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def game():
	return render_template('game.html')

@app.route('/guess', methods=['POST'])
def guess():

	session['num'] = random.randrange(1 ,101)
	print "Random #:", session['num']
	guess = int(request.form['guess'])
	print "Your number:", guess

	if session['num'] != random.randrange(1, 101):
		session['num'] = random.randrange(1 ,101)


	if guess < session['num']:
		session['guess'] = "too_low"
	elif guess > session['num']:
		session['guess'] = "too_high"
	else:
		session['guess'] = "correct"

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True)