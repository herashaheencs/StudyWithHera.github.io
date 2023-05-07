import bcrypt
from functools import wraps
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask import Flask

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yXR~XHH!jmN]LWX/,?RT'

valid_name='nit'
valid_pwhash ="patna"
lit_ans ="Romeo and Juliet"
math_ans="9"

def check_auth(username, password):
	
	if(username == valid_name and valid_pwhash == password):
		return True
	return False

def check_eng(lit):
	
	if(lit == lit_ans):
		return True
	return False

def check_math(math_begginer1):
	
	if(math_begginer1 == math_ans):
		return True
	return False

def requires_login(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		status = session.get('logged_in', False )
		if not status:
			return redirect( url_for('.root'))
		return f (*args, **kwargs)
	return decorated

def requires_lit(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		status = session.get('lit_in', False )
		if not status:
			return redirect( url_for('.english'))
		return f (*args, **kwargs)
	return decorated

def requires_math(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		status = session.get('math_in', False )
		if not status:
			return redirect( url_for('.math'))
		return f (*args, **kwargs)
	return decorated

@app.route('/logout/')
def logout():
	session ['logged_in'] = False
	return redirect(url_for('.root'))

@app.route("/secret/")
@requires_login
def secret():
	return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def root():
	if request.method == 'POST':
		user = request.form['username']
		pw = request.form['password']

		if check_auth(request.form['username'], request.form['password']):
			flash("You have logged in sucessfully")
			session['logged_in'] = True
			return render_template('index.html')
	return render_template('login.html')
		


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app . route ("/static-example/img")
def static_example_img () :
    start = "<img src" 
    url = url_for ('static', filename ='background.jpg')
    end = '" >'
    return start + url + end , 200

@app.route("/Home")
def home():
    return render_template("index.html")


@app.route("/Math", methods=['GET', 'POST'])
def math():
	if request.method == 'POST':
		mth = request.form['math_begginer1']

		if check_math(request.form['math_beginner1']):
			flash("Well done that is the correct answer")
			session['math_in'] = True

	return render_template("math.html")

@app.route("/English", methods=['GET', 'POST'])
def english():
	if request.method == 'POST':
		eng = request.form['lit']

		if check_eng(request.form['lit']):
			flash("Well done that is the correct answer")
			session['lit_in'] = True
			
	return render_template("english.html")


@app.route("/Science")
def science():
    return render_template("science.html")

@app.route("/History")
def history():
    return render_template("history.html")

@app.route("/Art")
def art():
    return render_template("art.html")

if __name__ == "__main__":
    app.run(debug=True)
