from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():

    return render_template ('home.html')

@app.route('/page2',methods=['POST'])
def process_form():

    Name = request.form['name']
    Email = request.form['email']
    print Name
    print Email
    return redirect ('/page3')

@app.route('/page3')
def page3():
    return render_template('page3.html')

app.run(debug=True)
