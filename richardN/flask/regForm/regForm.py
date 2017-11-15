from flask import Flask, render_template, redirect, request, flash
import re
app = Flask(__name__)
app.secret_key = 'iDontThinkSoSucka'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def home ():
    return render_template ('page1.html')

@app.route('/page2',methods=['POST'])
def survey ():
    error = False

    if len(request.form['email'])==0:
        flash('You SHALL NOT PASS!, this page >_< enter email')
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('umm... enter a real email.')
        error = True

	if len(request.form['firstName']) == 0:
		flash("HEY! enter a first name")
		error = True
	elif not request.form['firstName'].isalpha():
		flash("Umm... letters only")
		error = True

	if len(request.form['lastName']) == 0:
		flash("Yo! enter a last name")
		error = True
	elif not request.form['lastName'].isalpha():
		flash("Umm... letters only")
		error = True

    if not len(request.form['password']) > 8:
		flash("count! password must be > 8 characters")
		error = True
    elif not request.form['password']==request.form['confirmPassword']:
		flash("passwords dont match... try agina")
		error = True

    if error:
        return redirect('/')

    return render_template('page2.html')
    print formData


app.run(debug=True)
