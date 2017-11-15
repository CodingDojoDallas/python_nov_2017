##############################
### Load VEnv and Create the App File Structure / Template
##############################
## load flask venv
# navigate to your virtualenv folder and load it
$ source py2FlaskEnv/bin/activate #for mac
$ call py2FlaskEnv/Scripts/activate # for windows
# your terminal prompt should start with (py2FlaskEnv) after you successfully load
# you can deactivate your virtualenv with the command "deactivate"

## checking that your flask is installed properly
$ python # opens the python shell
> import flask 
> flask.__version__ #cheks the flask version)
> exit() #exits the python shell

## create app file structure
# if you do not have css or js or images you will not need the entire static folder
# File Structure:
- project name
  - server.py
  - templates
    - index.html
  - static
    - css
      - project.css
    - javascript  
      - project.js
    - images
      - image1.png
      - image2.png


## create server.py file with following template code, modifying route and method name as needed
from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():       
  return 'Hello World!'  # Return 'Hello World!' to the response.

app.run(debug=True)      # Run the app in debug mode.

## other libraries you may want to import:
from flask import Flask, request, render_template, redirect, session, flash
import re

## create templates subfolder
# add index.html and other html files inside

## run the app (I recommend running the app to make sure everything loads first before you start adding other code)
$ python server.py
# localhost:5000 should show

##############################
### Create the SQL layer 
##############################
## connect mamp and mysqlworkbench
# start your MAMP server
# start workbench
# make sure the connection for workbench is pointing to the same port as MAMP, you can create a connection on the top
  # half of the home page (at least for version 6.3.8)

## create your ERD diagram using mysqlworkbench and then create your database
# bottom half of workbench (at least for version 6.3.8) is for creating the ERD
# create the tables, relationships, set the name of your schema
# top menu -> database -> forward engineer # this will create your sql statements for making the database
# if your workbench is fully working... you can continue through the forward engineer prompt and let workbench 
  # make your database for you
# if your workbench is not fully working... you can copy the sql statements for creating the table and then create the tables
# using those statements in another program like sequelpro (you will have to make the right connections again)

## connect to your database
# go back to the homepage in mysqlworkbench and connect to the database 
# (you can either create a new connection or reuse an existing one, you can use the same connection for multiple projects and databases)
# under the schemas list you should be all to see all of your different databases
# double click on the database you want to work with to select it (it should highlight in bold after it is selected)

## add default seed data for your database 
# (do this for all of the tables you will need to display on the views of your application)
# Option 1:
# bring up the table you want to add data to by running a SELECT * FROM <tablename> query
# Example: SELECT * FROM users
# an empty table should pop up, you can write data directly into the rows of this table
# Option 2:
# Use an INSERT INTO SQL statement

## modifying a sql table (i.e adding a coulmn) 
# (note - it may be easier to just modify the erd and start over if you dont care about the data)
# you can go to your schema list, hover over the table you want to modify, and click the wrench button, from here you
# can add columns as well as add foreign keys if you go to the foreign key tab on the bottom (you will need to specify
  # the name of the foreign key (i.e. fk_posts_users), the referenced table, and what column on that table is being referenced)

## sample SQL statements

# Example 1
INSERT INTO profiles (description, user_id) VALUES ("myprofile", 5);

# Example 2
SELECT cities.name AS cities_name, countries.name AS country_name
FROM cities
LEFT JOIN countries
ON countries.id = cities.country_id
WHERE cities.name = "Kabul";

# Example 3
SELECT COUNT(cities.name) FROM cities;

# Example 4
# Use "NOW()"" to set timestamp for creating a SQL entry
INSERT INTO emailvaliddb.emails (address, updated_at) VALUES ('s1@example.com', NOW());

##############################
### Create your Server.py GET routes and html files
##############################

## create all the GET routes first, these will all render a template
# I recommend creating them such that they just display one word of html text first and loading it so that you know
# the route is working
@app.route('/')
def index():
    return render_template('index.html')

## build out html
# flesh out your html files so that they include all of your forms and fields etc, can use hard coded data first
# (see forms section below for syntax of building forms)

## add template pass through data (if needed)
# this is data where you assign the value in your server.py and then pass it to the html file as a parameter of render_template
# (see JINJA section below)

## add session display data (if needed)
# if you need to display session data, set some session data to a hardcoded number in your server.py method and then
# display that session data in you html file using jinja, and make sure that works before adding more complicated session data
# (see session section below)

## add database data (if needed)
# add and configure mysqlconnection.py file 
# add mysql code for server.py file
# Example
from mysqlconnection import MySQLConnector
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'emailvaliddb')
all_emails = mysql.query_db("SELECT * FROM emails")

@app.route('/friends/<id>/edit')  
def edit(id):
  query = "SELECT * FROM friends WHERE id = :id"
  data = {'id': id} #the blue id here matches to the orange id passed in the parameter of the method
  friend_array = mysql.query_db(query, data) # be aware of what datatype is being returned - in this case it is an array
  if len(friend_array) == 0:
    friend = None
  else:
    friend = friend_array[0]
  return render_template('edit.html', friend = friend)

# run a basic select SQL query and print out the result to your terminal to make sure everything is connected and working
# run the specific select SQL query you need, and again check that the result is what you want through the terminal
# display that data on your view page using JINJA and for loops as needed





##############################
### Create your Server.py POST routes
##############################
# the post routes handle your submitted form data, this includes creating, updating and deleting data
# you will usually be redirecting to another GET route after a post route. This means that after running all your 
# POST route code, you are sending a response to the client telling it to make another requset to another route 
# (usually a GET route) where you are going to render a template

## build the route and associated method first
@app.route('/process', methods=['POST'])
def process():
  first_name = request.form['first_name']
  return redirect('/')

## add validations (if needed)
if len(request.form['first_name']) < 1:
    flash("First Name cannot be empty!")

## creating
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
           }
    # Run query, with dictionary values injected into the query.
    x = mysql.query_db(query, data)
    return redirect('/')

## deleting
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

## updating
@app.route('/friends/<id>', methods=['POST'])
def update(id):
  query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
  data = {
           'first_name': request.form['first_name'], 
           'last_name':  request.form['last_name'],
           'email': request.form['email'],
           'id': id
         }
  mysql.query_db(query, data)
  return redirect('/')


##############################
### JINJA
##############################
@app.route('/user')
def user():
    name1 = "shane" # we set the string "shane" to a variable name name
    return render_template('user.html', name2=name1)
    ## passing in a variable to the template through render_template
    # the name1 on the right side of "name2=name1" is a reference to the variable "name1" we assigned in the line above
    # the name2 on the left side of "name2=name" is the name of the variable "name2" that is passed to our html
    # in practice we would likely just call name1 and name2 both "name" 
    
# in your html
{{some variable}} #Ex: <p>My name is {{name2}}</p> 
{%some expression%} # can be used for if statements of for loops

{% if x == 1 %}
  # do something
{% elif x == 2 %}
  # do something
{% endif %}

# the "with" command is used to set up a variable in jinja
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      <!-- do stuff with 'message' variable -->
    {% endfor %}        
  {% endif %}
{% endwith %}


# loading css, js, and images
<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_style_sheet.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='img/my_img.png') }}">

##############################
### Sessions
##############################

## Definition: 
# A session is a small piece of data that is passed back and forth between the client and the server. If you need to "remember"
# any information from one request to the next, without storing it in a database, such as that a user has logged in, you 
# will want to store that information in a session. You can then read that information from the session in a subsequent request

## Sessions are dictionaries <see flaskcheatsheet_dict_and_arrays> for more on the syntax of how to read and assign data to dictionaries>

## syntax for assigning data to a session
session['user_id'] = 5
session['fruits'] = [["pineapple", 5], ["orange", 3]]

# what the sesion data structure looks like
# session = {
#   "user_id" : 5
#   "fruits" : [
#     ["pineapple", 5], 
#     ["orange", 3]
#   ] 
# }

## clearing session data
session.clear()

## checking for NONE with a session
# prior to setting a value for a session key, the value defaults to None
# if you try to get the value when it doesn't exist (i.e. do "if session['counter'] == None:" when you have not assigned it yet) 
# Python will throw you an error, so you have to use session.get instead  
if session.get('counter') == None 


##############################
### Forms
##############################
# the action points to the route 
# Example edit form
<form action='/friends/{{friend['id']}}' method='POST'> # this is assuming a friend dictionary with the key of id is passed in
  <label for="email">Email:<input type="text" name="email" id="email"></label>
</form>

# button
<input type="submit" value="update">

##############################
### Debugging
##############################
$ pip install ipython # (terminal, w/ your enivironment up)
from IPython import embed # (add to the top of your .py file)
embed() # will create a breakpoint


##############################
### Bcrypt
##############################
pw_hash = bcrypt.generate_password_hash(registration_form_password) # this is how you generate a hashed_password
# you then store this hashed password into your database when creating the user

bcrypt.check_password_hash(stored_password, login_form_password) #returns true if the form_password is valid, false otherwise

##############################
### Flow
##############################
# http request comes in
# the url gets matched according to the available routes as designated by @app.route
# the method directly below the route is run

# that method renders a template or redirects to another route
# if it is redirecting to another route, the server is actually sending a response back to the client (browser)
# telling it to make another request to another url path, which will usually then render a template to display a view 
# to the browser

# if there is a form on the view that is rendered, that form can be submitted
# the form submission will create a new http request that once again matches to a specific route @app.route this time 
# with a methods=['POST']
# the method below it is run - usually processing some data and making a sql query
# this is usually followed with a redirect to another route




