from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')

@app.route('/')              
def index():

	friends = mysql.query_db("""select a.name as friend_name, a.age as friend_age, date_format(a.created_at, '%M %D %Y') as friends_since
								from users a 
								order by a.name;
							""")
	return render_template('index.html', friends = friends)      

@app.route('/process', methods=['POST'])
def processF():
   query = "INSERT INTO users (name, age, created_at) VALUES (:name, :age, NOW())"
   data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }
   mysql.query_db(query, data)
   return redirect('/') 
    
app.run(debug=True)