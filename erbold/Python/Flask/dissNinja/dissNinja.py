from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ninjas")
def group():

    return render_template("group.html")

@app.route("/ninjas/<color>")
def colors(color):

	if color == "blue":
		return render_template("blue.html")
	elif color == "red":
		return render_template("red.html")
	elif color == "orange":
		return render_template("orange.html")
	elif color == "purple":
		return render_template("purple.html")
	elif color != "red" "blue" "orange" "purple":
		return render_template("ninjas.html")

app.run(debug=True)
