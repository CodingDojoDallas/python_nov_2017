from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'newenglandclamchowder'

@app.route('/')
def counter():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/plustwo', methods=['POST'])
def plus_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
