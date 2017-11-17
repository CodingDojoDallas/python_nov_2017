from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def my_portfolio():
	return render_template('portfolio.html')

@app.route('/project')
def my_projects():
	return render_template('project.html')

@app.route('/about')
def  about_me():
	return render_template('aboutMe.html')

app.run(debug=True)



#def hellow_world():
#	return render_template('helloworld.html')
