from flask import Flask, render_template, redirect, session, request

import random


app = Flask(__name__)  

app.secret_key = 'OopsIDidItAgain'

@app.route('/')          
def home():
	if session.get('ranNum') == None:
		session['ranNum']=random.randrange(0,101)
		print session['ranNum']
	return render_template('index.html')

@app.route('/result', methods=['post'])          
def result():
	if int(request.form['guess'])==session['ranNum']:
		answer = "You Got it Biiiihhh! The number is "+str(session['ranNum'])
		return render_template('win.html', answer=answer, right=session['ranNum'])
	elif int(request.form['guess'])>session['ranNum']:
		answer = "Na Fam. Too High"
		return render_template('index.html', answer=answer)
	else:
		answer = "No, No, No. Too Damn Low"
		return render_template('index.html', answer=answer)

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)






