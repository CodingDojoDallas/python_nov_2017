from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5

app = Flask(__name__)
app.secret_key = 'OopsOneMoreTime'

mysql = MySQLConnector(app,'loginRegistration')

def registrationVal(form_data):
    errors = False

    if len(request.form['first_name']) <2:
        flash('First name cannot be empty')
        errors = True

    if len(request.form['last_name']) <2:
        flash('Last name cannot be empty')
        errors = True

    if len(request.form['email']) <1:
        flash('Email cannot be empty')
        errors = True

    if len(request.form['password']) <1:
        flash('Password cannot be empty')
        errors = True

    if request.form['passwordC'] != request.form['password']:
        flash('passwords must match')
        errors = True
    print errors
    return errors    

@app.route('/')
def index():
                               
    return render_template('index.html') 

@app.route('/register', methods=['POST'])
def register():

    errors = registrationVal(request.form)

    if errors == True:
        return redirect('/')
    else:
        h_pw = md5.new(request.form['password']).hexdigest()

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name': request.form['last_name'],
                 'email': request.form['email'],
                 'password': h_pw,
               }

        print 'got all the information'
        mysql.query_db(query, data)
        return redirect('/success')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM users WHERE users.email = :email AND users.password = :password"
    data = { 'email': email, 'password': password }
    user = mysql.query_db(query, data)
    print user

    if user != []:
        print 'hello'
        return redirect('/success')
    else:
        flash('Oh No Big Fella. What is you doin?')
        return redirect ('/')
    

@app.route('/success')
def home():

    return render_template('success.html')

    
app.run(debug=True)
