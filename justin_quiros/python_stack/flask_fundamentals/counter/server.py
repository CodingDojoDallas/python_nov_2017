from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
	if "counter" not in session:
		session['counter'] = 0
	else:
		session['counter'] += 1
	return render_template('index.html')

@app.route('/add2', methods=['POST'])
def add2():
	session['counter'] += 1
	return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
	session.clear()
	return redirect("/")


app.run(debug=True)