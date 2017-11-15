from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
app.secret_key = 'iDontThinkSoSucka'

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
    if len(formData['Name'])<1:
        flash('You SHALL NOT PASS!, this page >_<')
        return redirect('/')
    if len(formData['Comment'])<1:
        flash('You SHALL NOT PASS!, this page >_<')
        return redirect('/')
    if len(formData['Comment'])>120:
        flash('You SHALL NOT PASS!, this page >_<')
        return redirect('/')
    else:
        flash('You may continue')
        return render_template ('page2.html', form = formData)
    print formData


app.run(debug=True)
