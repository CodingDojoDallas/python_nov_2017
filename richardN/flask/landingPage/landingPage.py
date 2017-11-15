from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('home.html')


@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def dojo():
    print 'new'
    return render_template('dojos.html')


app.run(debug=True)
