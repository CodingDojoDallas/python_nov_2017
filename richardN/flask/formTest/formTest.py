from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("first.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users', methods=['POST'])#must match the html
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   return redirect('/')

app.run(debug=True) # run our server
#Important! Always redirect after handling POST data to avoid data being handled more than once! Try it for yourself. Create a template with a form, then have that form submit to the '/users' route from the code snippet above. Create another HTML document, success.html. Change the create_user method as follows:
@app.route('/users', methods=['POST'])
def create_user():
   name = request.form['name']
   email = request.form['email']
	 # Here's the line that changed. We're rendering a template from a post route now.
   return render_template('success.html')

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template("user.html")
app.run(debug=True)
