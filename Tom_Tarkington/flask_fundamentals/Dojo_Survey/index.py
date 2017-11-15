from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "newenglandclamchowder"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def post_data():
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comments = request.form['comments']

   if len(name) < 1:
    flash("Name cannot be empty!") 
    return redirect('/')

   if len(comments) < 1:
    flash("Comments cannot be empty!") 
    return redirect('/')

   if len(comments) > 120:
    flash("Comments must be less than 120 characters!") 
    return redirect('/')

   return render_template('result.html', name=name, location=location, language=language, comments=comments)


app.run(debug=True)
