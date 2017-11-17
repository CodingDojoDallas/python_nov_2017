from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
	return '<p>Welcome to my portfolio! My name is Anna!</p>'


@app.route('/projects')
def projects():
	return render_template('portfolio.html')


@app.route('/about')
def about():
	return render_template('about.html')

app.run(debug=True)