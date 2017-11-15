from flask import Flask, render_template, request, redirect, session, flash
import md5
import re
import os, binascii # include this at the top of your file

app = Flask(__name__)
password = 'password'
hashed_password = md5.new(password).hexdigest()
print hashed_password
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'log_reg_db')

app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET'])	
def home():
	return render_template('index.html')

@app.route('/success', methods=['GET'])
def success():
	return render_template('success.html')

@app.route('/process', methods=['POST'])
def process():
	if request.form['action'] == 'reg':
		if len(request.form['f_name']) < 2:
			flash('First Name not Valid', 'f_name')
		if len(request.form['l_name']) < 2:
			flash('Last Name not Valid', 'l_name')
		if len(request.form['email']) < 1:
			flash("You need to have an email", "email")
		elif not EMAIL_REGEX.match(request.form['email']):
			flash('Invalid Email Address!', "email")
		if len(request.form['password']) < 8:
			flash('Password is not Valid', 'password')
		if request.form['password'] != request.form['password_comp']:
			flash('Passwords do not match', 'password_comp')
		f_name = request.form['f_name']
		l_name = request.form['l_name']
		email = request.form['email']
		password = request.form['password']
		salt = binascii.b2a_hex(os.urandom(15))
		hashed_pw = md5.new(password + salt).hexdigest()
		insert_query = "INSERT INTO log_reg (f_name, l_name, email, password, salt, created_at, updated_at) VALUES (:f_name, :l_name, :email, :hashed_pw, :salt, NOW(), NOW())"
		query_data = { 'f_name': f_name, 'l_name': l_name, 'email': email, 'hashed_pw': hashed_pw, 'salt':salt}
		mysql.query_db(insert_query, query_data)
		return redirect('/')
	if request.form['action'] == 'login':
		password = md5.new(request.form['password']).hexdigest()
		email = request.form['email']
		#log_reg_query = "SELECT * FROM log_reg where log_reg.email = :email AND log_reg.password = :password"
		log_reg_query = "SELECT * FROM log_reg WHERE log_reg.email = :email LIMIT 1"
		query_data = { 'email': email}
		log_reg = mysql.query_db(log_reg_query, query_data)
		if len(log_reg) != 0:
			print "test"
			encrypted_password = md5.new(password + log_reg[0]['salt']).hexdigest()
			if log_reg[0]['password'] == encrypted_password:
				return redirect('/success')
			else:
				flash("Invalid Password")
				return redirect('/')
		else:
			flash("Invalid Email")
			return redirect('/')
				
		# do the necessary logic to login if the user exists, otherwise redirect to login page with error message<br>

	



app.run(debug=True)






