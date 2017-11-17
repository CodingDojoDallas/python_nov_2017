from flask import Flask ,render_template, request ,redirect,session
app = Flask(__name__)
app.secret_key="ThisisSecret"

@app.route('/')
def index():
	if session.get('counter') == None: 
		session['counter'] =2

	return render_template('index.html')

@app.route('/addcount',methods=['POST'])
def addcounter():
	session['counter'] +=2
	return redirect('/')

@app.route('/resetcount',methods=['POST'])
def reset():
	session['counter'] = 1
	return redirect('/')

app.run(debug=True)	

