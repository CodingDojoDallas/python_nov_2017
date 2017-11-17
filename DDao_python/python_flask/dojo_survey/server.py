from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def dojo_survey():
	return render_template('dojo.html')

@app.route('/result', methods=['POST'])
def results():

	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template('result.html', name=name, location=location, language=language, comment=comment)
	return redirect('/')

app.run(debug=True)
