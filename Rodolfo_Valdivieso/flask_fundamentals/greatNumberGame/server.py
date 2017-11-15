from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
           
@app.route('/')              
def game():
    if (session.get('number') == None):
    	session['number'] =  random.randint(1, 10)
    return render_template('index.html', message="", number=session['number'])  

@app.route('/guess', methods=['POST'])              
def guess():

	num1 = int(request.form['numberInserted'])
	num2 = int(session['number'])
	
	if(num1 == num2):
		message = "You WON!!!!, the number was:"
	elif(num1 > num2):
		message = "You are too high....."
	else:
		message = "You are too low....."
	return render_template('index.html', message=message, number=session['number']) 

@app.route('/won', methods=['POST'])              
def won():
	session.pop('number')
	return game()
	#session.pop('number') 
	#return render_template('index.html', number=session['number']) 

app.run(debug=True)      # Run the app in debug mode.