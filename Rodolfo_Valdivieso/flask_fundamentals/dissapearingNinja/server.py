from flask import Flask, render_template, request, redirect
app = Flask(__name__)    
           
@app.route('/')              
def index():
	return render_template('index.html', message="No Ninjas Here!!!!")      

@app.route('/ninjas', methods=['POST'])
def processF():
   return render_template('ninjas.html', image="tmnt.png")   

@app.route('/goBack')              
def goback():
	return render_template('index.html', message="No Ninjas Here!!!!") 

@app.route('/ninjas/<color>')
def colors(color):
    name = ""
    if color == "blue":
    	image = "leonardo.jpg"
    	name = "Leonardo"
    elif color == "orange":
    	image = "michelangelo.jpg"
    	name = "Michelangelo"
    elif color == "red":
    	image = "raphael.jpg"
    	name = "Raphael"
    elif color == "purple":
    	image = "donatello.jpg"
    	name = "Donatello"
    else:
    	image = "notapril.jpg"
    	name = "That Color does not exist!!!"

    return render_template('ninjas.html', image=image, name=name)

app.run(debug=True)      # Run the app in debug mode.