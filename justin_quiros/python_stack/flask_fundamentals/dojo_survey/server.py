from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comments = request.form['comments']
	if len(request.form['name']) < 1:
		flash("You did not enter your name.")
	elif len(request.form['comments']) > 120:
		flash("This comment box has a 120 character max.")
	return redirect('/')
	# return render_template("result.html", name = name, location = location, language = language, comments = comments)

app.run(debug=True)