from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template("index.html")

@app.route('/ninjas')
def ninjaInfo():
    return render_template("ninjas.html")


@app.route('/dojos/new')
def form():
    return render_template("dojos.html")

app.run(debug=True)