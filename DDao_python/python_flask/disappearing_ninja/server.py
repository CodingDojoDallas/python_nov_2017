from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjas():
	return render_template('ninjas.html')

@app.route('/ninja/<color>')
def show_turtle(color):
		if color == "blue":
			return render_template('blue.html')
		elif color == "orange":
			return render_template('orange.html')
		elif color == "red":
			return render_template('red.html')
		elif color == "purple":
			return render_template('purple.html')
		elif color !="red" "purple" "blue" "orange":
			return render_template('hack.html')


app.run(debug=True)