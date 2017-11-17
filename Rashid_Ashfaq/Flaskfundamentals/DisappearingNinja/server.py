from flask import Flask ,render_template
app =Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html",display ="NO NINJA HERE")
@app.route('/ninja')
def ninja():
	return render_template('ninja.html')

@app.route('/ninja/blue')
def ninjablue():
	return render_template('blue.html')

@app.route('/ninja/orange')
def ninjaorange():
	return render_template('orange.html')

@app.route('/ninja/red')
def ninjared():
	return render_template('red.html')

@app.route('/ninja/purple')
def ninjpurple():
	return render_template('purple.html')
@app.route('/ninja/<username>')	
def notapril(username):
	return render_template("notapril.html", username=username)

app.run(debug=True)