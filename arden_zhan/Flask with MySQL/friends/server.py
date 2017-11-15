from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends') #name of database schema

@app.route('/')
def index():
    query = "SELECT * FROM  friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (fullname, age, created_at, updated_at) VALUES (:fullname, :age, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
        'fullname': request.form['fullname'],
        'age': request.form['age']
        }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')
    
app.run(debug=True)
