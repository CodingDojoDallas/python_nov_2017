from flask import Flask, render_template, request, redirect


app = Flask(__name__)    


@app.route('/')          

def survey():
	return render_template('index.html')    

@app.route('/result', methods=['POST'])

def result():
	print 'got post info'
	name=request.form['name']
	emails=request.form['emails']
	movie=request.form['movie']
	meals=request.form['meals']
	dish=request.form['dish']
	date=request.form['date']
	print name
	print emails
	print movie
	print meals
	print dish
	print date

	return render_template('info.html')

app.run(debug=True)     