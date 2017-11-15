from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'mydb')

@app.route('/')              
def index():
  if (session.get('email') == None):
      session['email'] = ""
  if (session.get('message') == None):
      session['message'] = ""
  return render_template('index.html', email=session['email'], message=session['message'])

@app.route('/result')              
def result():
  emails = mysql.query_db("""select a.email as email, date_format(a.created_at, '%M %D %Y') as date
                from users a 
                order by a.name;
              """)
  return render_template('result.html', emails=emails, email=session['email'])      

@app.route('/process', methods=['POST'])
def processF():
  error = 0
  email = request.form['email']
  session['email'] = email
  if len(email) < 1 :
    flash("Email cannot be empty!")
    error = 1
  elif not EMAIL_REGEX.match(email):
    flash("Invalid Email Address!")
    error = 1

  if error == 1:
   return redirect('/') 
  else:
   query = "INSERT INTO users (email, created_at) VALUES (:email, NOW())"
   data = {
             'email': request.form['email']
           }
   mysql.query_db(query, data)

   return redirect('/result') 

@app.route('/delete', methods=['POST'])
def delete():
   query = "delete from users"
   session['email'] = ""
   session['message'] = "Table deletion successfull!!!"
   mysql.query_db(query)
   return redirect('/') 

@app.route('/goback')
def goback():
  session['email'] = ""
  session['message'] = ""
  return redirect('/') 


app.run(debug=True)