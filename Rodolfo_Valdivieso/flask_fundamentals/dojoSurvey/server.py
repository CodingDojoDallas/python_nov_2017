from flask import Flask, render_template, request, redirect
app = Flask(__name__)    
           
@app.route('/')              
def index():
	return render_template('index.html')      

@app.route('/process', methods=['POST'])
def processF():
   print "Got Post Info"
   first_name = request.form['firstName']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   return render_template('result.html', name=first_name, location=location, language=language, comment=comment)   

@app.route('/goBack')              
def goback():
	return render_template('index.html') 

app.run(debug=True)      # Run the app in debug mode.