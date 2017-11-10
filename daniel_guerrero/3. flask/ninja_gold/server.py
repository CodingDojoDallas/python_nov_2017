from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)

app.secret_key = "my_super_secret_key"

@app.route('/')
def index():
	return render_template('index.html')
#================================================
@app.route('/process_money', methods=['POST'])
def gold():
	if 


	return redirect('/')



app.run(debug=True