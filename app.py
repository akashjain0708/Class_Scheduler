from flask import Flask, render_template, request, json, flash, redirect, url_for
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient
from werkzeug import generate_password_hash, check_password_hash

def connect():
# Substitute the 5 pieces of information you got when creating
# the Mongo DB Database (underlined in red in the screenshots)
# Obviously, do not store your password as plaintext in practice
    connection = MongoClient("ds049651.mongolab.com",49651)
    handle = connection["scheduler"]
    handle.authenticate("akash22jain","Urgointobemad1")
    return handle

app = Flask(__name__)
mongo = PyMongo(app)
handle = connect()

@app.route("/")
def main():
	
	#post = {"name":"Akash",
			#"text":"Hey!"}
	#posts = handle.userData
	#post_result = posts.insert_one(post)	
	document = handle.userData.find_one({"email": "abc"});
	#print(document)
	#print(document["password"])
	return render_template('index.html');

@app.route("/signUp")
def signUp():
	return render_template("signUp.html");

@app.route("/login", methods=['POST'])
def login():
	user_name = request.form['inputName']
	user_email = request.form['inputEmail']	
	user_password = request.form['inputPassword']
	user_confirm_password = request.form['confirmPassword']
	# validate the received values	
	if not (user_name and user_email and user_password and user_confirm_password):		
		return json.dumps({'status':'ERROR', 'errorMessage':'Enter all fields!'})
	elif user_password!=user_confirm_password:
		return json.dumps({'status':'ERROR', 'errorMessage':"Passwords do not match!"})
	else:
		post = {"name": user_name, "password":generate_password_hash(user_password), "email":user_email}
		post_result = handle.userData.insert_one(post)
		return json.dumps({'status':'OK', 'redirect':url_for('schedule')})
		#return json.dumps({'html':'<span>All fields good !!</span>'})
		#flash("All fields good! Thank you for signing up!")			

@app.route('/loginCheck', methods=['POST'])
def loginCheck():
	user_email = request.form['inputEmail']	
	user_password = request.form['inputPassword']	
	# validate the received values	
	if not (user_name and user_email and user_password and user_confirm_password):		
		return json.dumps({'status':'ERROR', 'errorMessage':'Enter all fields!'})	
	else:
		document = handle.userData.find_one({"email": user_email});
		if check_password_hash(document["password"], user_password):
			return json.dumps({'status':'OK', 'redirect':url_for('schedule')})
		else:
			return json.dumps({'status':'ERROR', 'errorMessage':"Passwords do not match for the user! Try again"})

@app.route('/schedule')
def schedule():
	return render_template('schedule.html')

if __name__ == '__main__':
	app.run()