from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
	image = ""

	if "disp" not in session:
		session['disp'] = "Take a guess!"

	if "rand" not in session:
		session['rand'] = random.randrange(0,101)

	if "number" not in session:
		session['number'] = 0


	if session['number'] == 0:
		session['disp'] = session['disp']
	elif session['number'] < session['rand']:
		image = "too_low.jpg"
		# session ['disp'] = 'static/image/too_low.jpg'
	elif session['number'] > session['rand']:
		image = "too_high.jpg"
		# session['disp'] = 'static/image/too_high.jpg'
	else:
		image = "thats_right.jpg"
		# session['disp'] = 'static/image/thats_right.jpg'

	print session['number'] 
	print session['rand']
	return render_template('index.html', image = image )

@app.route('/guess', methods=['GET', 'POST'])
def guess():
	session['number'] = int(request.form['number'])
	return redirect('/')

@app.route('/again', methods=['POST'])
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)