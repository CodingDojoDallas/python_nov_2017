from flask import Flask, flash, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'dope'

def countLetters(word):
    count = 0
    for c in word:
        count += 1
    return count

@app.route("/")
def index():

    # if session.get('num') == None:
    #     setSession()
    # else:
    #     pass
    # print session['num']	
    return render_template("index.html")


@app.route("/answer", methods = ['POST'])
def result():
	First_name = request.form['fname']
	Last_name = request.form['lname']
	Comment = request.form['comment']
	
	if First_name == '':
		flash('error blank', 'error')
		return redirect('/')

	if Last_name == '':
		flash('error blank', 'error') 
		return redirect('/')

	session['comment'] = request.form['comment']
	comment = countLetters(session['comment'])
	print comment
	if comment > 120:
		flash('length error', 'error')
		return redirect('/')


	return render_template("answer.html", First_name = First_name, Last_name = Last_name, Comment = Comment)
	return redirect('/')

app.run(debug=True)
