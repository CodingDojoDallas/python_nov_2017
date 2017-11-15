from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'

@app.route('/')              
def index():
	return render_template('index.html')      

@app.route('/process', methods=['POST'])
def processF():
	print "Got Post Info"
	first_name = request.form['firstName']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	error = 0
	if len(first_name) < 1 :
		flash("Name cannot be empty!")
		error = 1
	if location=="":
		flash("You must pick a Location!")
		error = 1
	if language=="":
		flash("You must chosse a language!")
		error = 1
	if len(comment) < 1:
		flash("Comment cannot be empty!")
		error = 1
	if len(comment) > 10:
		flash("Comment cannot be more than 10 characters!")
		error = 1

	if error != 0:
		return render_template('index.html', name=first_name, location=location, language=language, comment=comment)
	else:
		return render_template('result.html', name=first_name, location=location, language=language, comment=comment)   

@app.route('/goBack')              
def goback():
	return render_template('index.html') 

app.run(debug=True)      # Run the app in debug mode.