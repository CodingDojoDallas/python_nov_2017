from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def home ():

    return render_template ('page1.html')

@app.route('/page2',methods=['POST'])
def survey ():

    formData = {
        'Name': request.form['name'],
        'Location': request.form['location'],
        'FavLang': request.form['FavLang'],
        'Comment': request.form['Comment']
    }
    print formData

    return render_template ('page2.html', form = formData)

app.run(debug=True)
