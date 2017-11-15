from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random
#use hidden values
@app.route('/')
def home():
	if 'activities' not in session:
		session['activities'] = []
	if "gold" not in session:
		session["gold"] = 0

	if 'farm' not in session:
		session['farm'] = 0

	if 'cave' not in session:
		session['cave'] = 0

	if 'house' not in session:
		session['house'] = 0

	if 'casino' not in session:
		session['casino'] = 0

	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	if request.form['building'] == 'farm':
		session['farm'] = random.randrange(10, 21)
		session['gold'] += session['farm']
		session['activities'] = 'Earned money from farm'
	elif request.form['building'] == 'cave':
		session['cave'] = random.randrange(5, 11)
		session['gold'] += session['cave']
		session['activities'] = 'Earned money from cave'
	elif request.form['building'] == 'house':
		session['house'] = random.randrange(2, 6)
		session['gold'] += session['house']
		session['activities'] = 'Earned money from house'
	elif request.form['building'] == 'casino':
		session['casino'] = random.randrange(-50, 51)
		session['gold'] += session['casino']
		session['activities'] = 'Earned money from casino'
	return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)