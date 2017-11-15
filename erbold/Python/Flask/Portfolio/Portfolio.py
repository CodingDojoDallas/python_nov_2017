from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def root():
	return render_template('Root.html')
# app.run(debug=True)

@app.route('/projects')

def projects():
	return render_template('Projects.html')
# app.run()


@app.route('/about')

def about():
	return render_template('About.html')
app.run(debug=True)
