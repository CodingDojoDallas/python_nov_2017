from flask import Flask, render_template, request, redirect
app = Flask(__name__)    

# our index route will handle rendering our form                 
@app.route('/')              
def index():
	return render_template('index.html')      


@app.route('/process', methods=['POST'])
def processF():
   print "Got Post Info"
   name = request.form['firstName']
   last = request.form['lastName']
   print name
   print last
   # redirects back to the '/' route
   return redirect('/')

app.run(debug=True)      # Run the app in debug mode.