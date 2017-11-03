from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<choice>')
def color(choice):
    if choice == "blue":
        url = "../static/images/leonardo.jpg"
    elif choice == "purple":
        url = "../static/images/donatello.jpg"
    elif choice == "orange":
        url = "../static/images/michelangelo.jpg"
    elif choice == "red":
        url = "../static/images/raphael.jpg"
    else:
        url = "../static/images/notapril.jpg"
    return render_template('ninja.html', extra_url=url)

app.run(debug=True)
