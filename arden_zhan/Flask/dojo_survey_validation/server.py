from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    
    yourname = request.form['yourname']
    location = request.form['location'] 
    faveLang = request.form['faveLang']
    comment = request.form['comment']

    errors = False

    if len(yourname) < 1:
        flash("Name cannot be empty!")
        errors = True
        
    if len(comment) < 1:
        flash("Comment cannot be empty!")
        errors = True
        
    if len(comment) > 120:
        flash("Comment cannot be > 120 chars")
        errors = True

    if errors == True:
        return redirect('/')

    flash("Data validated")
    return render_template("result.html", 
        yourname = yourname, 
        location = location,
        faveLang = faveLang,
        comment = comment)

app.run(debug = True)
