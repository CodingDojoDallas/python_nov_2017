from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
	query = "SELECT * FROM full_friends"
	full_friends = mysql.query_db(query)
	print full_friends
	return render_template('index.html', full_friends = full_friends)

@app.route('/friend', methods=['POST'])
def friend():
	query = "INSERT INTO full_friends (name, age, friend_since) VALUES (:name, :age, NOW())"
	data = {
		'name': request.form['name'],
		'age':  request.form['age']
		}
	mysql.query_db(query, data) 

	return redirect('/')

app.run(debug=True)