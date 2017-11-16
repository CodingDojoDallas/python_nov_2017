
from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
import sys

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key='theyMayTakeOurLandButTheyWillNeverTakeOurFreedom!'

mysql = MySQLConnector(app, 'emailval')

@app.route("/")
def index():
	return render_template("page0.html")

@app.route("/page1", methods=["POST"])
def process():
	if len(request.form['email']) == 0:
		flash("email can't be empty")
		return redirect('/')
	if not EMAIL_REGEX.match(request.form['email']):
		flash("email not valid ")
		return redirect('/')

	mysql.query_db("INSERT INTO emails(email, created_at) Values(:email, now())", {"email": request.form['email']})
	return redirect('/page1')

@app.route('/page1')
def sucess():
	data = mysql.query_db("SELECT id, email, DATE_FORMAT(created_at, '%m/%e/%y %l:%i %p') AS date FROM emails")

	return render_template("page1.html", data = data)

@app.route('/delete', methods=['POST'])
def delete():
	id = int(request.form['id'])
	mysql.query_db("DELETE FROM emails WHERE id = :id", {"id": id })
	return redirect('/page1')
app.run(debug=True)
