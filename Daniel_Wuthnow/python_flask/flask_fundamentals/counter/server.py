from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

#adds one on refresh
@app.route('/')
def welcome():
	if 'counter' not in session:
		session['counter']=0
	else:
		session['counter']+=1
	return render_template('index.html')

#adds 1 from the refresh and one from the button
@app.route('/addtwo', methods=['POST'])
def addtwo():
	if 'counter' not in session :
		session['counter']=0
	else:
		session['counter']+=1
	return redirect('/')



#clears the session
@app.route('/clear', methods=['POST'])
def clear():
	session.clear()
	return redirect('/')
# @app.route('/reset')
# def reset():
# 	session['counter'] = 0
# 	return redirect('/') 


app.run(debug=True)