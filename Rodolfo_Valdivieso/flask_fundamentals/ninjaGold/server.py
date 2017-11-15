from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
           
@app.route('/')              
def game():
    if (session.get('gold') == None):
    	session['gold'] = 0 
    if (session.get('activities') == None):
    	session['activities'] = []
    if (session.get('class') == None):
    	session['class'] = []
    return render_template('index.html', gold=session['gold'])  

@app.route('/process_money', methods=['POST'])              
def process_money():
	building   = request.form['building']
	goldEarned = 0
	activity   = ""
	if building == "farm":
		goldEarned = random.randint(10, 20)
	elif building == "cave":
		goldEarned = random.randint(5, 10)
	elif building == "house":
		goldEarned = random.randint(2, 5)
	elif building == "casino":
		goldEarned = random.randint(-50, 50)

	if goldEarned >= 0:
		activity = "Earned: " + str(goldEarned) + " Golds from the " + building + "! (" + str(datetime.datetime.now()) +")"
		session['class'].append("green")
	else:
		activity = "Enter a Casino  and Lost: " + str(goldEarned) + " ..Ouch... "  + " (" + str(datetime.datetime.now())+")"
		session['class'].append("red")

	session['gold'] = session['gold'] + goldEarned
	session['activities'].append(activity)

	print session['class']

	if session['gold'] < 0:
		session['gold'] = 0
	return render_template('index.html', gold=session['gold'], activities=session['activities'],  classes=session['class']) 

@app.route('/reset', methods=['POST'])              
def won():
	session.pop('gold')
	session.pop('activities')
	session.pop('class')
	return game()

app.run(debug=True)      # Run the app in debug mode.