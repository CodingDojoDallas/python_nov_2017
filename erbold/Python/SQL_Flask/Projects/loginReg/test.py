def validate_login(form_data):
	errors = {}

	#email
	if len(form_data['email']) == 0:
		errors['email'] = "Email is required."
	#password
	if len(form_data['password']) == 0:
		errors['password'] = "Pasword is required."
	return errors 


@app.route('/login', methods = ['POST'])
def login():

	email = request.form['email']
	password = request.form['password']

	query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
	data = {'email': email}
	user = mysql.query_db(query, data)

	if len(user) != 0:
		encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
		if user[0]['hashed_pw'] == encrypted_password:
			return redirect('/success')
		else:
			flash('invalid login homie!')
			return redirect('/')
	else:
		flash('invalid login homie!')
		return redirect('/')

app.run(debug=True)
