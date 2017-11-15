from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'SekritKey'

@app.route('/')
def index():
    if session.get('num') == None:
        session['num'] = random.randrange(0, 101)
    print "number to guess is", session['num']

    if session.get('guess') == None:
        # Just started game, no guess yet
        session['guess'] = 0
    
    print "guessed number is", session['guess']

    return render_template("index.html", guess=int(session['guess']), num=int(session['num']))

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = request.form['guess']
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('num') #remove num
    session.pop('guess')
    return redirect('/')

app.run(debug = True) # run our server
