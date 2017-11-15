from flask import Flask, render_template


app = Flask(__name__)    


@app.route('/')          
def landing():
	return render_template('index.html')    

@app.route('/ninja')
def ninjas():
  return render_template('ninjas.html')

@app.route('/ninja/orange')
def orange():
  return render_template('orange.html')

@app.route('/ninja/red')
def red():
  return render_template('red.html')

@app.route('/ninja/blue')
def blue():
  return render_template('blue.html')

@app.route('/ninja/purple')
def purple():
  return render_template('purple.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


app.run(debug=True)     