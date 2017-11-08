from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')

def noNinjas():
    return render_template('page0.html')

@app.route('/ninja')

def ninjas():
    return render_template('ninja.html')

@app.route('/ninja/<turtle>')

def turtle

app.run(debug=True)
