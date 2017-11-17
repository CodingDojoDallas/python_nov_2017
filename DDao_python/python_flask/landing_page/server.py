from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/ninjas')
def ninjas_info():
	return render_template('ninjas.html')

@app.route('/dojos/new', methods=['GET'])
def dojo_new():

	return render_template('dojo.html')
	return redirect('/')


app.run(debug=True)