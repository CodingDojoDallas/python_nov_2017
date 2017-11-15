from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)

app.secret_key = "my_super_secret_key"

valid = True

@app.route('/')
def index():
	return render_template('index.html')
#==================================================


@app.route('/result', methods=['POST'])
def result():
	content = {
		"name": request.form['name'],
		"location": request.form['location'],
		"fav": request.form['fav'],
		"comment": request.form['comment']
		}
	if len(content["name"]) < 1:
		flash("Name is required")
		return redirect("/")
	if len(content["comment"]) > 120:
		flash("Comment is too long!")
		return redirect("/")
	elif len(content["comment"]) < 1:
		flash("Need to add a comment!")
		return redirect("/")
	if valid:
		return render_template("result.html", content=content)


app.run(debug=True)