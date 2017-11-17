from flask import Flask, render_template, redirect, request, session

import random

app = Flask(__name__)

app.secret_key = 'numbergame'

@app.route('/')

def randomnumber():

    if 'randnum' not in session:

        session['randnum'] = random.randint(1,100)

    return render_template('index.html')

@app.route('/guessnumber', methods=['POST'])

def guessnumber():

    print "Randum Number=", session['randnum']

    print "My Number=", request.form['number']

    if int(request.form['number']) == session['randnum']:

        return render_template('index.html', result=request.form['number']+" was the number!", color="green",flag="True")

    elif int(request.form['number']) > session['randnum']:

        return render_template('index.html', result=request.form['number']+" was Too High!", color="red")

    else:

        return render_template('index.html', result=request.form['number']+" was Too Low!", color="red")

@app.route('/reset')

def reset():

    session.pop('randnum')

    return redirect('/')

app.run(debug=True)