from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "KeepItSecret!"

@app.route('/')
def dojo_survey():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def results():

	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']

	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
	elif len(request.form['comment']) > 120:
		flash("Comment cannot be more than 120 characters.")
	else:
	 return render_template('result.html', name=name, location=location, language=language, comment=comment)
	
	
	return redirect('/')

@app.route('/reset')
def back():
	return render_template('index.html')

app.run(debug=True)