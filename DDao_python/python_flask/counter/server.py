from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "ThisisSecret"


@app.route('/')
def index():
	if(session['counter'] != 0):
		session['counter'] += 2
	
	return render_template('counter.html')

@app.route('/reload', methods=['POST'])
def reload():
	session['counter'] += 2

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['counter'] = 0

	return redirect('/')

app.run(debug=True)