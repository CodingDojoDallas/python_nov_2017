from flask import Flask, render_template ,request ,redirect,session, flash
app = Flask(__name__)
app.secret_key ="KeepItSecretKeepItSafe"
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	name =request.form['name']
	if len(request.form['name'])<1:
		flash("Name cannot be empty")
		return redirect('/')	
	location =request.form['location']
	language=request.form["language"]
	comment=request.form['comment']
	if len(request.form['comment'])<1:
		flash("Comment can not be empty")
		return redirect('/')
	if len(comment)>120:
		flash("Comment no more then 120 character ")
		return redirect('/')

	return render_template('result.html',name= name,location=location,language=language,comment=comment)
	return render_template('index.html')
@app.route('/back')
def back():
	return render_template('index.html')

app.run(debug=True)

