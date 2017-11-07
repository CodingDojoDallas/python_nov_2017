from flask import Flask, render_template, redirect, session, request, flash

import random

app = Flask(__name__)  

app.secret_key = 'OopsIDidItForreal'

@app.route('/')          
def home():
	if session.get('goldNum')==None:
		session['goldNum']=0
		print session['goldNum']
	if session.get('activities')==None:
		session['activities']= ''
	return render_template('index.html')

@app.route('/getgold', methods=['POST'])          
def result():

	if request.form['building']=='farm':
		newGold=random.randrange(10,21)
		session['goldNum'] += newGold
		session['activities'] +='\nEarned '+str(newGold)+' gold from the farm!'
		print 'Earned '+str(newGold)+' gold from the farm!'
	elif request.form['building']== 'cave':
		newGold=random.randrange(5,11)
		session['goldNum'] += newGold
		print 'Earned '+str(newGold)+' gold from the cave!'
	elif request.form['building']== 'home':
		newGold=random.randrange(2,6)
		session['goldNum'] += newGold
		print 'Earned '+str(newGold)+' gold from home!'
	elif request.form['building']== 'casino':
		newGold=random.randrange(-50,51)
		session['goldNum'] += newGold
		if newGold>=0:
			print 'Earned '+str(newGold)+' gold from the casino!'
		else:
			print 'Lost '+str(abs(newGold))+' gold from the casino...DAMN!'

	return redirect('/')

app.run(debug=True)






