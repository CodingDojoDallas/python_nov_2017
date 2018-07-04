from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
	print request.form['first_name']
	print request.form['last_name']
	print request.form['occupation']
	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
	data = {
		'first_name': request.form['first_name'],
		'last_name':  request.form['last_name'],
		'occupation': request.form['occupation']
		}
	mysql.query_db(query, data)

	return redirect('/')

app.run(debug=True)