from app import app
from flask import render_template,redirect, request, flash,g,session,url_for
from models import *

@app.route('/', methods = ["GET", "POST"])
@app.route('/index', methods = ["GET," "POST"])
def index():
	return render_template("index.html")
	#return get_all_meetups()
	#return get_all_attendees('2')
@app.route("/getallmeetups")
def getallmeetups():
	return get_all_meetups()

@app.route("/signup", methods=["GET","POST"])
def signup():
	return render_template("signup.html")

@app.route("/signedup", methods=["GET","POST"])
def signedup():
	username = request.form['username']
	password = request.form['password']

	add_user(username, password)

	return (username)

@app.route("/meetup", methods = ["GET", "POST"])
def meetup():
	return render_template("meetup.html")

@app.route("/createmeetup", methods = ["GET", "POST"])
def createmeetup():
	starttime = request.form['starttime']
	endtime = request.form['endtime']
	classname = request.form['classname']
	subject = request.form['subject']
	createdby = request.form['createdby']

	add_meetup(starttime, endtime, classname, subject, createdby)

	return(starttime)

@app.route("/attend", methods = ["GET", "POST"])
def attend():
	return render_template("attend.html")

@app.route("/doRSVP", methods = ["GET", "POST"])
def doRSVP():
	uid = request.form['uid']
	eid = request.form['eid']

	set_going(uid, eid)
	return eid

@app.route("/checkattendance", methods = ["GET", "POST"])
def checkattendance():
	return render_template("checkattendance.html")

@app.route("/getattend", methods = ["GET", "POST"])
def getattend():
	uid = request.form['uid']
	eid = request.form['eid']

	return str(is_going(uid, eid))