from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SecretKey"
mysql = MySQLConnector(app,'emailsdb') #name of database schema

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails = emails, success_email = session['email'])

# BONUS DELETE
# @app.route('/remove_email/<email_id>', methods=['POST'])
# def delete(email_id):
#     query = "DELETE FROM emails WHERE id = :id"
#     data = {'id': email_id}
#     mysql.query_db(query, data)
#     return redirect('/')

@app.route('/process', methods=['POST'])
def create():
    email = request.form['email']
    session['email'] = email
    if not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        return redirect('/')
    
    else:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email': request.form['email']
            }
        mysql.query_db(query, data)
        return redirect('/success')
    
app.run(debug=True)
