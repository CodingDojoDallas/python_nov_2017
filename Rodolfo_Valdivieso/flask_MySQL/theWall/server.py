from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import datetime
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'wall')

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

@app.route('/wall')              
def result():
  
  query = """select a.id, concat(a.first_name, ' ', a.last_name) as poster_name, date_format(b.created_at, '%M %D %Y %T') as date_posted, b.id as post_id, b.message as post_message, c.id as comment_id, c.comment as comment, date_format(c.created_at, '%M %D %Y  %T') as date_comment, concat(d.first_name,' ',d.last_name) as comment_by
             from users a join messages b on a.id = b.user_id
                     left join comments c on b.id = c.message_id
                     left join users    d on d.id = c.user_id
             order by b.id desc , c.id desc ;
          """
  resultados=mysql.query_db(query)

  return render_template('result.html', first_name=session['first_name'], last_name=session['last_name'], success=session['success'], user_id=session['user_id'], results=resultados)      

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
    return redirect('/wall')
  else:
    return redirect('/')


@app.route('/post', methods=['POST'])
def post():
  error = 0
  post = request.form['post']

  if len(post) < 1 :
    flash("Post cannot be empty!")
    error = 1

  query = "INSERT INTO messages (user_id, message, created_at) VALUES (:user_id, :message, NOW())"
  data = {
             'user_id': session['user_id'], 
             'message': post
         }
  mysql.query_db(query, data)

  return redirect('/wall')

@app.route('/delete', methods=['POST'])
def delete():

  query = """select id from messages 
            where id = :post_id and (TIMESTAMPDIFF(MINUTE, created_at, now())) < 30"""
  data = {
             'post_id': request.form['post_id']
         }
  ableTodelete = mysql.query_db(query, data)
  if ableTodelete != []:
    query = """delete from comments 
               where message_id = :post_id """
    data = {
             'post_id': request.form['post_id']
         }
    mysql.query_db(query, data)

    query = """delete from messages 
               where id = :post_id """
    data = {
             'post_id': request.form['post_id']
         }
    mysql.query_db(query, data)
  else:
    flash("Cannot delete message more than 30 minutes old!!!")
  return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
  error = 0
  comment = request.form['comment']

  if len(comment) < 1 :
    flash("Comments cannot be empty!")
    error = 1

  query = "INSERT INTO comments (message_id, user_id, comment, created_at) VALUES (:message_id, :user_id, :comment, NOW())"
  data = {
             'message_id': request.form['post_id'],
             'user_id': session['user_id'], 
             'comment': comment
         }
  mysql.query_db(query, data)

  return redirect('/wall')


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

   query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
   data = {
             'first_name': request.form['first_name'], 
             'last_name': request.form['last_name'], 
             'email': request.form['email'],
             'password': password_hashed
           }
   mysql.query_db(query, data)
   userid = getId()

   return redirect('/wall') 


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
  user = mysql.query_db("select * from users where email = '"+session['email']+"'")
  if not user:
    return "0" 
  else:
    return "1"

def getPassword():
  password = mysql.query_db("select password from users where email = '"+session['email']+"'")
  if password == []:
    password=""
  else:
    password = password[0]['password']
  return password

def getId():
  userid = mysql.query_db("select id, first_name, last_name from users where email = '"+session['email']+"'")
  if userid == []:
    session['user_id'] = ""
    session['first_name'] = ""
    session['last_name'] = ""
  else:
    session['user_id'] = userid[0]['id']
    session['first_name'] =  userid[0]['first_name']
    session['last_name'] =  userid[0]['last_name']
    userid = userid[0]['id']
  return userid
  

app.run(debug=True)