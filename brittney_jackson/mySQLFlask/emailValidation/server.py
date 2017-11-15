from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app,'eval')

@app.route('/')
def index():
    query = "SELECT * FROM emails"                          
    emails = mysql.query_db(query)                           
    return render_template('index.html', all_emails=emails) 

@app.route('/success', methods=['POST'])
def create():
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (email, NOW(), NOW())"
    data = {
             'email': request.form['email'],
           }
    query2 = "SELECT * FROM emails"                          
    emails = mysql.query_db(query2)

    print 'got the email address'
    mysql.query_db(query, data)
    return render_template('success.html', all_emails=emails)
    



app.run(debug=True)
