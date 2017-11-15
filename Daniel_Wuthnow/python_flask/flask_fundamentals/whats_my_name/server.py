from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def welcome():
	return render_template('index.html')


@app.route('/process', methods= ['POST'])
def name():
	print request.form['name']
	return redirect('/')

app.run(debug=True)