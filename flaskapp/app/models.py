import sqlite3 as sql
import json
import collections

def add_user(username, password):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO users VALUES (null,?,?)", (username, password))
		con.commit()

def add_meetup(classname, subject, starttime, endtime, createdby):
	 with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO meetups VALUES (null,?,?,?,?,?)", (classname, subject, starttime, endtime, createdby))
		con.commit()

def set_going(uid, eid):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO RSVPS VALUES (?,?)", (eid, uid))
		con.commit()

def is_going(uid, eid):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM RSVPS WHERE uid = ? AND eid = ?", (uid, eid))
		if not(cur.fetchall()):
			return False
		else:
			return True

def get_all_meetups():
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM meetups;")
		rs = list(cur.fetchall())

		meetuplist = []
		for row in rs:
			mdict = collections.OrderedDict()
			mdict['eid'] = row[0]
			mdict['starttime'] = row[1]
			mdict['endtime'] = row[2]
			mdict['classname'] = row[3]
			mdict['subject'] = row[4]
			mdict['createdby'] = row[5]

			meetuplist.append(mdict)


		return(json.dumps(meetuplist))

def get_all_attendees(eid):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM RSVPS WHERE eid = ?;",eid)
		rs = list(cur.fetchall())

		listofattendees = []
		for row in rs:
			listofattendees.append(getUsernameFromUID(row[1])) #change to getUsername(uid)

		return (json.dumps(listofattendees))

def getUsernameFromUID(uid):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT username FROM users WHERE uid = ?;",str(uid))
		rs = cur.fetchall()
		if not rs:
			return "Error"
		else:
			return rs[0][0]


#def exists_user():
#def delete_meetup():
#def delete_user():