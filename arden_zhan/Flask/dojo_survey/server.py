from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods = ['POST'])
def result():
    return render_template("result.html", 
        yourname = request.form['yourname'], 
        location = request.form['location'], 
        faveLang = request.form['faveLang'], 
        comment = request.form['comment'])

app.run(debug = True)
