from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html", link = "img/tmnt.png")

@app.route('/ninja/<color>')
def ninjaColor(color):
    if color == "blue": 
        link = "img/leonardo.jpg"
        altdesc = "blue leonardo"
    elif color == "orange": 
        link = "img/michelangelo.jpg"
        altdesc = "orange michelangelo"
    elif color == "red":
        link = "img/raphael.jpg"
        altdesc = "red raphael"
    elif color == "purple":
        link = "img/donatello.jpg"
        altdesc = "purple donatello"
    else: 
        link = "img/notapril.jpg"
        altdesc = "not april"

    return render_template("ninja.html", link = link, altdesc = altdesc)

app.run(debug = True)
