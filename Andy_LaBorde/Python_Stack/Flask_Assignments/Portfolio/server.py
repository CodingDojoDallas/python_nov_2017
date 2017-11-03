from flask import Flask,  render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/projects')
def my_projects():
	return render_template('project.html')

@app.route('/aboutMe')
def about_me():
	return render_template('aboutMe.html')



app.run(debug=True)
