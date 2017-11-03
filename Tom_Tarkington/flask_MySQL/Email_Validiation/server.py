from flask import Flask, request, redirect, render_template, session, flash
import re, md5, os, binascii
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
app.secret_key = "key"

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

@app.route('/email', methods=['POST'])
def register():
    valid = True

    data = {
    'email': request.form['email'].lower(),
    }

    if len(data['email']) < 1:
        flash("Please enter an email address")
    elif not EMAIL_REGEX.match(data['email']):
        flash("Please enter a valid email")

    if valid:
        # data['password'] = md5.new(data['password']
        query = "SELECT * FROM users WHERE email=:email"
        check = mysql.query_db(query, data)

        if len(check) == 0:
            query = "INSERT INTO users (email) VALUES (:email)"
            mysql.query_db(query, data)
            return redirect('/')
        else:
            flash("That email already exists!")

    return redirect('/')


app.run(debug=True)
