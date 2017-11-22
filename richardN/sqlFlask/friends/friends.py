
from flask import Flask, render_template, redirect, request, flash
from mySqlConnection import MySQLConnector
import re
import sys

def log(obj):
	print(obj)

NAME_REGEX = re.compile(r'^[a-zA-Z-]+$')

app = Flask(__name__)
app.secret_key="whoDoYouThinkYouArelookingInHere"

mysql = MySQLConnector(app, 'mydb')

@app.route("/")
def index():
	query = "SELECT * FROM friends"
	data = mysql.query_db(query)
	return render_template("page1.html", data=data)

@app.route('/process', methods=["POST"])
def process():
	log(request.form)
	error = False
	if len(request.form['first_name']) == 0:
		flash("enter a first name")
		error = True
	if not NAME_REGEX.match(request.form['first_name']):
		flash("name is invalid")
		error = True
	if len(request.form['last_name']) == 0:
		flash("enter a last name")
		error = True
	if not NAME_REGEX.match(request.form['last_name']):
		flash("name is invalid")
		error = True
	if len(request.form['age']) == 0:
		flash("enter an age")
		error = True
	elif not request.form['age'].isdigit():
		flash("age must be a number")
		error = True
	elif int(request.form['age']) < 0:
		flash("Age is invalid")
		error = True

	if error:
		return redirect("/")

	query = 'INSERT INTO friends(first_name, last_name, age, since) VALUES(:first_name, :last_name, :age, now())'
	data = {"first_name":request.form["first_name"],"last_name":request.form["last_name"], "age":request.form["age"]}
	mysql.query_db(query, data)
	return redirect('/')



app.run(debug=True)
