from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'full_friends')
# an example of running a query
print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():




	query = "SELECT * FROM friends"                           # define your query
	friends = mysql.query_db(query)                           # run query with query_db()
	return render_template('index.html', all_friends=friends) # pass data to our template


	
	# friends = mysql.query_db("SELECT * FROM friends")
	# print friends
	# return render_template('index.html') # pass data to our template


@app.route('/process', methods=["GET", "POST"])
def process():
	query = "INSERT INTO friends (name, age, friend_since) VALUES (:name, :age, NOW())"

	data = {
			'name': request.form['name'],
			'age': request.form['age']
	}

	mysql.query_db(query, data)

	return redirect('/')



app.run(debug=True)


