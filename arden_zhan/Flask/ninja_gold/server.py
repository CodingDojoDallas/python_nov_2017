from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'SekritKey'

@app.route('/')
def index():
    if session.get('gold') == None:
        session['gold'] = 0
    print "Gold:", session['gold']

    if session.get('activities') == None:
        session['activities'] = ""
    print "Activities:", session['activities']

    return render_template("index.html", 
        gold = session['gold'],
        activities = session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == "farm":
        tempFarm = random.randrange(10,21)
        session['gold'] += tempFarm
        session['activities'] += "\nEarned {} golds from the farm!".format(tempFarm)
    elif request.form['building'] == "cave":
        tempCave = random.randrange(5,11)
        session['gold'] += tempCave
        session['activities'] += "\nEarned {} golds from the cave!".format(tempCave)
    elif request.form['building'] == "house":
        tempHouse = random.randrange(2, 6)
        session['gold'] += tempHouse
        session['activities'] += "\nEarned {} golds from the house!".format(tempHouse)
    elif request.form['building'] == "casino":
        tempCasino = random.randrange(-50, 51)
        session['gold'] += tempCasino
        if tempCasino > 0: 
            session['activities'] += "\nEarned {} golds from the casino!".format(tempCasino)
        elif tempCasino < 0:
            session['activities'] += "\nEntered a casino and lost {} golds... Ouch..".format(tempCasino)



    return redirect('/')

app.run(debug = True) # run our server
