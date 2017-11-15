# Input:

# -A form submission

# Output:

# -Presents the submitted data on a results page

# Logic:

# -The goal is to get me familiar with sending POST requests through a form and displaying
# that information




from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods = ['POST'])
def result():

	First_name = request.form['fname']
	Last_name = request.form['lname']
	print First_name
	print Last_name
	return render_template("results.html", First_name = request.form['fname'], Last_name = request.form['lname'])

app.run(debug=True)
