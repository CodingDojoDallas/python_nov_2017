from flask import Flask, render_template, session, redirect
app = Flask(__name__)

@app.route('/')
def noNinjas():
    return render_template('page0.html')

@app.route('/ninja')
def ninjas():
    showAll= True
    return render_template('ninja.html',showAll=showAll)

@app.route('/ninja/<turtle>')
def color(turtle):
    showAll= False
    return  render_template('ninja.html', turtle=turtle, showAll=showAll)

app.run(debug=True)
