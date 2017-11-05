from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
	if "gold" not in session:
		session['gold'] = 0
	if "farm" not in session:
		session['farm'] = 0
		print session['farm']
	if "cave" not in session:
		session['cave'] = 0
		print session['cave']
	if "house" not in session:
		session['house'] = 0
		print session['house']
	if "casino" not in session:
		session['casino'] = 0
		print session['casino']
	if "x" not in session:
		session['x'] = ""

	return render_template('index.html')

@app.route('/process_money', methods=['GET', 'POST'])
def process():
	if request.form['action'] == 'farm':
		session['farm'] = random.randrange(10,21)
		session['gold'] += session['farm']
		session['x'] = "Earned {} golds from the {}".format(session['farm'], request.form['action'])
	if request.form['action'] == 'cave':
		session['cave'] = random.randrange(5,11)
		session['gold'] += session['cave']
		session['x'] = "Earned {} golds from the {}".format(session['cave'], request.form['action'])
	if request.form['action'] == 'house':
		session['house'] = random.randrange(2,6)
		session['gold'] += session['house']
		session['x'] = "Earned {} golds from the {}".format(session['house'], request.form['action'])
	if request.form['action'] == 'casino':
		session['casino'] = random.randrange(-51,51)
		session['gold'] += session['casino']
		session['x'] = "Earned {} golds from the {}".format(session['casino'], request.form['action'])
		
	return redirect('/')

@app.route('/again', methods=['POST'])
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)