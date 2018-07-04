1) 
$ python server.py
Traceback (most recent call last):
  File "server.py", line 2, in <module>
    from mysqlconnection import MySQLConnector
  File "C:\Users\Erbold Uran\Documents\Coding Dojo\python_nov_2017\erbold\Python\SQL_Flask\Projects\friends\mysqlconnection.py", line 2, in <module>
    from flask_sqlalchemy import SQchemy
ImportError: cannot import name SQchemy
(flaskEnv)


fix - Typed SQLAlchemy correctly

2)
OperationalError: (_mysql_exceptions.OperationalError) (1049, "Unknown database 'db'")

fix - Converted db back into a value after making it a string

3)
NameError: global name 'result' is not defined

fix - I had to set it equal to the original variable name so that i could link it with 
the rest of the program
