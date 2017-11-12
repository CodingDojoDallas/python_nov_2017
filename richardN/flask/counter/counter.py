
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hidden'


@app.route('/')
def index():
    if session.get('count')==None:
        session['count']=0
    session['count'] += 1
    return render_template('home.html', count=session['count'])

@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = -1
    return redirect('/')

app.run(debug = True)
