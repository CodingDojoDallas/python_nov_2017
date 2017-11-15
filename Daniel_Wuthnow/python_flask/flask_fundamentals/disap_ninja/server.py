from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route('/')
def welcome():
	return render_template('index.html', message= "No ninjas here")

@app.route('/ninja')
def ninja():
	return render_template('ninja.html', img= 'tmnt.png')

@app.route('/ninja/<color>')
def color(color):
	if color == 'blue':
		return render_template('ninja.html', img= 'leonardo.jpg')
	elif color == 'purple':
		return render_template('ninja.html', img= 'donatello.jpg')
	elif color == 'orange':
		return render_template('ninja.html', img= 'michelangelo.jpg')
	elif color == 'red':
		return render_template('ninja.html', img= 'raphael.jpg')
	else:
		return render_template('ninja.html', img= 'notapril.jpg')




app.run(debug=True)