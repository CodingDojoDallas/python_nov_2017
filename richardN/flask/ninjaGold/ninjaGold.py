from flask import Flask, render_template, session,request, redirect
import random
import datetime
app = Flask(__name__)
app.secret_key= 'whatdafrack'

@app.route('/')
def index():
    if 'bank' not in session:
        session['bank'] = 0
    if 'adventure' not in session:
        session['adventure'] = []
    return render_template('money.html')

@app.route('/processGold', methods=['POST'])
def process():

    if request.form['building'] == "farm":
        new= random.randrange(-50,100)


    elif request.form['building'] == "cave":
        new= random.randrange(-100,200)

    elif request.form['building'] == "house":
        new= random.randrange(-10,50)

    else:
        new= random.randrange(-700,700)

    session['bank'] += new
    # time= datetime.now().strftime("%Y/%m/%d %I:%m %p")
    if new>=0:
        adventure="Earned () from the () ().format(new, request.from['building'])"
    else:
        adventure="Entered () and lost () gold. HAHA... ()".format(request.form['building'],-1*new)
    session['adventure'].append(adventure)

    return redirect('/')

app.run(debug=True)
