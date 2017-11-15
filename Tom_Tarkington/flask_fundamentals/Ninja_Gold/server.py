from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "newenglandclamchowder"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    activity = request.form['activity']
    if activity == "farm":
        income = random.randint(10,20)
        activity = "Earned " + str(income) + " gold from the farm! (" + str(datetime.now()) + ")"
    elif activity == "cave":
        income = random.randint(5,10)
        activity = "Earned " + str(income) + " gold from the cave! (" + str(datetime.now()) + ")"
    elif activity == "house":
        income = random.randint(2,5)
        activity = "Earned " + str(income) + " gold from the house! (" + str(datetime.now()) + ")"
    elif activity == "casino":
        income = (random.randint(0,100)-50)
        activity = "Won " + str(income) + " gold from the casino! (" + str(datetime.now()) + ")"
    
    if 'gold_total' not in session:
        session['gold_total'] = income
    else:
        session['gold_total'] += income
    
        
    if 'activities' not in session:
        session['activities'] = [activity]
    else:
        session['activities'].append(activity)
    return redirect('/')
    
@app.route('/reset')
def reset():
    session['gold_total'] = 0
    session['activities'] = []
    return redirect('/')

app.run(debug=True)
