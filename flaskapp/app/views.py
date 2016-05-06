from app import app
from flask import render_template, redirect, request, flash, g, session, url_for, send_file
from models import *

app.secret_key = "donttellanyonemysecret"

# First Button: Homepage
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if 'username' in session:
        return render_template("index.html",username =session['username'])
    else:
        return render_template("index.html")

# return get_all_meetups()
# return get_all_attendees('2')
# return get_meetup_info(2)

@app.route("/css/<css>")
def style_render(css):
    return render_template("css/%s"%css)

@app.route("/images/<image>")
def image_render(image):
    filename = ('templates/images/%s'%image)
    return send_file(filename,mimetype='image/jpeg')

@app.route("/js/<js>")
def js_render(js):
    return render_template("js/%s"%js)

@app.route("/js/moment-develop/moment.js")
def moment_js_render():
    return render_template("/js/moment-develop/moment.js")

@app.route("/bootstrap/js/<js>")
def bootstrap_js_render(js):
    return render_template("/bootstrap/js/%s"%js)

@app.route("/bootstrap/dist/bootstrap.min.js")
def bootstrapminjs():
    return render_template("bootstrap/dist/js/bootstrap.min.js")

@app.route("/bootstrap-datetimepicker.min.js")
def timepickerjs():
    return render_template("bootstrap-datetimepicker.min.js")

# Second Button
@app.route("/meetup", methods=["GET", "POST"])
def meetup():
    defaultlat=40.8199813
    defaultlng=-73.9498308
    if 'username' in session:
        return render_template("meetup.html", username=session['username'],lat=defaultlat,lng=defaultlng)

    return render_template("meetup.html",lat=defaultlat,lng=defaultlng)

@app.route("/createmeetup", methods=["GET", "POST"])
def createmeetup():
    starttime = request.form['starttime']
    endtime = request.form['endtime']
    classname = request.form['classname']
    subject = request.form['subject']
    createdby = request.form['createdby']
    add_meetup(starttime, endtime, classname, subject, createdby)

    if 'username' in session:
        return render_template("createdmeetup.html", username=session['username'])
    return render_template("createdmeetup.html")

# Third Button
@app.route("/attend", methods=["GET", "POST"])
def attend():
    if 'username' in session:
        return render_template("attend.html", username=session['username'])
    return render_template("attend.html")

@app.route("/doRSVP", methods=["GET", "POST"])
def doRSVP():
    uid = request.form['uid']
    eid = request.form['eid']
    set_going(uid, eid)
    return eid

@app.route("/doRSVPJSON", methods=["GET", "POST"])
def doRSVPJSON():
    uid = request.args.get('uid', 0, type=int)
    eid = request.args.get('eid', 0, type=int)

    set_going(uid, eid)
    return "RSVPed"

@app.route("/unRSVP", methods = ["GET", "POST"])
def unRSVP():
    uid = request.args.get('uid', 0, type=int)
    eid = request.args.get('eid', 0, type=int)

    set_not_going(uid, eid)
    return "unRSVPed"
    

# Fourth Button
@app.route("/checkattendance", methods=["GET", "POST"])
def checkattendance():
    if 'username' in session:
        return render_template("checkattendance.html",username=session['username'])
    return render_template("checkattendance.html")


# Fifth Button
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if 'username' in session:
        return render_template("signup.html",username=session['username'])
    return render_template("signup.html")

@app.route("/signedup", methods=["GET", "POST"])
def signedup():
    username = request.form['username']
    password = request.form['password']
    session['username'] = username
    session['logged_in'] = True
    add_user(username, password)
    return render_template("signedup.html",username=session['username'])


# Sixth Button
@app.route("/login", methods=["GET","POST"])
def login():
    if 'username' in session:
        return render_template("login.html",username=session['username'])
    else:
        return render_template("login.html")

@app.route("/loggedin", methods=["GET","POST"])
def loggedin():
    logUser = request.form['username']
    logPass = request.form['password']
    loginStatus = True
    # loginStatus = confirmUserPass(logUser,logPass)
    if loginStatus == True:
        session['username'] = logUser
        return render_template("loggedin.html",username=logUser)
    else:
        return render_template("loggedin.html",error="Bad user or password")


@app.route("/getattend", methods=["GET", "POST"])
def getattend():
    uid = request.form['uid']
    eid = request.form['eid']
    return str(is_going(uid, eid))

@app.route("/getallmeetups")
def getallmeetups():
    return get_all_meetups()

@app.route("/minfo/", methods=["GET", "POST"])
def minfo():

    return render_template("getmeetupinfo.html")


@app.route("/_minfo")
def _minfo():
    a = request.args.get('a', 0, type=int)
    return (json.dumps(get_meetup_info(a)))

@app.route("/meetupinfo<int:eid>", methods = ["GET", "POST"])
def meetupinfo(eid):
    mdict = get_meetup_info(eid)
    if (not mdict):
        return "Error!"

    #TODO: get these from json
    #eid= mdict['eid']
    classname = mdict['classname']
    subject=mdict['subject']
    starttime=mdict['starttime']
    endtime=mdict['endtime']
    coordinator=getUsernameFromUID(mdict['createdby'])
    lat=mdict['latitude']
    lng=mdict['longitude']

    tempuid = "2"

    if 'username' in session:
        return render_template("meetup.html", username=session['username'],meetid=eid, classname = classname, subject = subject, starttime=starttime, endtime=endtime, coordinator=coordinator, lat=lat, lng=lng,
        uid = tempuid, attending = is_going(tempuid, eid))

    return render_template("meetupinfo.html", meetid=eid, classname = classname, subject = subject, starttime=starttime, endtime=endtime, coordinator=coordinator, lat=lat, lng=lng,  
        uid = tempuid, attending = is_going(tempuid, eid))
