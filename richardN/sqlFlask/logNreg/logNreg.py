from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re, os, binascii, hashlib, sys

app = Flask(__name__)
app.secret_key = 'chillyWIllYisDa$hitt'
mysql = MySQLConnector (app, )
