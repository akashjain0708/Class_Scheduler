from flask import Flask, render_template, request
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient

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
	
	post = {"name":"Akash",
			"text":"Hey!"}
	posts = handle.userData
	post_result = posts.insert_one(post)	
	return render_template('index.html');

@app.route("/signUp")
def signUp():
	return render_template("signUp.html");

@app.route("/login", methods=['POST'])
def login():
	user_email = request.form['inputEmail']
	user_password = request.form['inputPassword']
	user_confirm_password = request.form['confirmPassword']
	if user_password != user_confirm_password:
		flash('Passwords do no match!')	

if __name__ == '__main__':
	app.run()
