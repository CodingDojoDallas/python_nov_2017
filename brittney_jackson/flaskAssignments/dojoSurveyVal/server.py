from flask import Flask, render_template, request, redirect, flash, session


app = Flask(__name__)  

app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')          

def survey():
	return render_template('index.html')    

@app.route('/info', methods=['POST'])

def result():
	if len(request.form['name']) <1:
		flash('Name cannot be empty')

	if len(request.form['date']) <1:
		flash('Perfect date cannot be empty')

	else:
		return redirect('/')

	return render_template('info.html', name=request.form['name'], email=request.form['email'], movie=request.form['movie'], meals=request.form['meals'], dish=request.form['dish'], date=request.form['date'])

app.run(debug=True)     