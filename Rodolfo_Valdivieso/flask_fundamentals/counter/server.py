from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
           
@app.route('/')              
def count():
    if (session['counter'] != None):
        session['counter'] =  session['counter'] + 1
    else:
        session['counter'] =  1
    return render_template('index.html', counter=session['counter'])  

@app.route('/add', methods=['POST'])              
def count2():
    session['counter'] = session['counter'] + 2
    return render_template('index.html', counter=session['counter'])   

@app.route('/reset', methods=['POST'])              
def count3():
    session['counter'] = 0
    return render_template('index.html', counter=session['counter'])  

app.run(debug=True)      # Run the app in debug mode.