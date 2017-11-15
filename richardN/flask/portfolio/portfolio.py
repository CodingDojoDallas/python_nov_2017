from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def Hi():
    return render_template('portfolio.html')

@app.route('/fml')
def fml():
    return render_template('fml.html')

@app.route('/frack')
def frack():
    return render_template('frack.html')

app.run(debug=True)
