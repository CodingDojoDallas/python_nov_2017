from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", message = "No Ninjas Here")

@app.route('/ninja')
def allninja():
	return render_template("ninja.html", image = "tmnt.png")

@app.route('/ninja/<color>')
def ninja(color):
	if color == "blue":
		return render_template("ninja.html", image = "leonardo.jpg")
	elif color == "orange":
		return render_template("ninja.html", image = "michelangelo.jpg")
	elif color == "red":
		return render_template("ninja.html", image = "raphael.jpg")
	elif color == "purple":
		return render_template("ninja.html", image = "donatello.jpg")
	else:
		return render_template("ninja.html", image = "notapril.jpg")


app.run(debug=True)