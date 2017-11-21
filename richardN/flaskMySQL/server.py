from flask import Flask
# import the Connector function
from mySQLconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print mysql.query_db("SELECT * FROM users")
config = {
    'host': 'localhost',
    'database': db, # we got db as an argument
    'user': 'root',
    'password': 'fml',
    'port': '3306' # change the port to match the port your SQL server is running on
}

app.run(debug=True)
