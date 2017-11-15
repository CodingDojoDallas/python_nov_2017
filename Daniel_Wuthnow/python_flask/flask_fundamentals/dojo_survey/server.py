from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def welcome():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		return redirect('/')
	# else:
	# 	flash('Hello {} it is nice to meet you').formate(request.form['name'])
	# if len(request.form['comment']) < 1:
	# 	flash('Please give a comment.')
	elif len(request.form['comment']) > 120:
		# return redirect('/')
		flash('Your comment is to long, please shorten it.')
		return redirect('/')
	# else:
	# 	flash('Thank you for your comment')
	return render_template('result.html', location= location,language= language)

app.run(debug=True)