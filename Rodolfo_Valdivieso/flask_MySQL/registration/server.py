from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import datetime
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'mydb')

@app.route('/')              
def index():
  if (session.get('success') == None):
      session['success'] = ""
  if (session.get('first_name') == None):
      session['first_name'] = ""
  if (session.get('last_name') == None):
      session['last_name'] = ""
  if (session.get('email') == None):
      session['email'] = ""
  if (session.get('user_id') == None):
      session['user_id'] = ""
  if (session.get('login') == None):
      session['login'] = ""
  return render_template('index.html', success=session['success'], first_name=session['first_name'], last_name=session['last_name'] , email=session['email'], login=session['login'], user_id=session['user_id'])

@app.route('/result')              
def result():
  return render_template('result.html', first_name=session.get('first_name'), last_name=session.get('last_name'), success=session.get('success'), user_id=session['user_id'])      

@app.route('/login')              
def login():
  session['login'] = "1"
  return redirect('/')

@app.route('/register')              
def register():
  session['login'] = "0"
  return redirect('/')

@app.route('/logincheck', methods=['POST'])              
def logincheck():
  #go and check in the DB if client exist
  email     = request.form['email']
  session['email'] = email
  session['user_id'] = ""

  password = md5.new(request.form['password']).hexdigest()
  error = 0

  #validations here
  if len(email) < 8 :
    flash("Email at least 8 chars long!")
    error = 1
  elif not EMAIL_REGEX.match(email):
    flash("Invalid Email Address format!")
    error = 1

  if error == 0:
    #check if user exists
    if exist() != "1":
      error = 1
      flash("Email address does not exist!")
    else:
      #check password
      password_hashedDB = getPassword()
      if (password_hashedDB != password):
        error = 1
        flash("Incorrect Password!")

  if error == 0:
    userid = getId()
    return redirect('/result')
  else:
    return redirect('/')



@app.route('/process', methods=['POST'])
def processF():
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  email     = request.form['email']
  password = request.form['password']
  password2 = request.form['password2']
  error = 0
  
  
  session['first_name'] = first_name
  session['last_name'] = last_name
  session['email'] = email
  session['login'] = "0"


  if len(first_name) < 2 :
    flash("First Name cannot be empty and at least 2 characters!")
    error = 1
  elif any(map(str.isdigit, str(first_name))):
    flash('First Name cannot contain Numbers.')
    error = 1
  if len(last_name) < 2 :
    flash("Last Name cannot be empty and at least 2 characters!")
    error = 1
  elif any(map(str.isdigit, str(last_name))):
    flash('Last Name cannot contain Numbers.')
    error = 1
  if len(email) < 1 :
    flash("Email cannot be empty!")
    error = 1
  elif not EMAIL_REGEX.match(email):
    flash("Invalid Email Address!")
    error = 1
  else: #it means email has a correct format
    if exist() == "1":
      flash("Email Already Exist!")
      error = 1

  if len(password) < 8:
    flash("Password must be at least 8 char long!")
    error = 1
  elif not any(map(str.isupper, str(password))):
    flash('Your password needs at least 1 capital.')
    error = 1
  elif not any(map(str.isdigit, str(password))):
    flash('Your password needs at least 1 number.')
    error = 1
  elif password != password2:
    flash("Password is not equal to Confirm Password!")
    error = 1
  
  if error == 1:
   return redirect('/') 
  else:
   password_hashed = md5.new(password).hexdigest()

   session['success'] = "1"
   session['user_id'] = ""

   query = "INSERT INTO forms (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
   data = {
             'first_name': request.form['first_name'], 
             'last_name': request.form['last_name'], 
             'email': request.form['email'],
             'password': password_hashed
           }
   mysql.query_db(query, data)
   userid = getId()

   return redirect('/result') 


@app.route('/goback', methods=['GET'])
def goback():
  session['success'] = ""
  session['first_name'] = ""
  session['last_name'] = ""
  session['email'] = ""
  session['user_id'] = ""
  session['login'] = ""
  return redirect('/') 

@app.route('/reset', methods=['GET'])
def reset():
  session['success'] = ""
  session['first_name'] = ""
  session['last_name'] = ""
  session['email'] = ""
  session['user_id'] = ""
  session['login'] = "0"
  return redirect('/') 


def exist():
  user = mysql.query_db("select * from forms where email = '"+session['email']+"'")
  if not user:
    return "0" 
  else:
    return "1"

def getPassword():
  password = mysql.query_db("select password from forms where email = '"+session['email']+"'")
  if password == []:
    password=""
  else:
    password = password[0]['password']
  return password

def getId():
  userid = mysql.query_db("select id from forms where email = '"+session['email']+"'")
  if userid == []:
    session['user_id'] = ""
  else:
    session['user_id'] = userid[0]['id']
    userid = userid[0]['id']
  return userid
  

app.run(debug=True)