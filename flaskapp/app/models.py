import sqlite3 as sql
import json
import collections
import os


def add_user(username, password):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES (null,?,?)", (username, password))
        con.commit()


def add_meetup(classname, subject, starttime, endtime, createdby, lat, lon):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO meetups VALUES (null,?,?,?,?,?,?,?)", (classname, subject, starttime, endtime, createdby, lat, lon))
        con.commit()


def set_going(uid, eid):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO RSVPS VALUES (?,?)", (eid, uid))
        con.commit()
        
def set_not_going(uid, eid):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM RSVPS WHERE eid = ? and uid = ?", (eid, uid))
        con.commit()


def is_going(uid, eid):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM RSVPS WHERE uid = ? AND eid = ?", (uid, eid))
        if not (cur.fetchall()):
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
            #mdict['coordinator'] = row[6]
            mdict['latitude'] = row[6]
            mdict['longitude'] = row[7]

            meetuplist.append(mdict)

        return (meetuplist)


def get_all_attendees(eid):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM RSVPS WHERE eid = ?;", eid)
        rs = list(cur.fetchall())

        listofattendees = []
        for row in rs:
            listofattendees.append(getUsernameFromUID(row[1]))  # change to getUsername(uid)

        return (json.dumps(listofattendees))


def getUsernameFromUID(uid):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT username FROM users WHERE uid = ?;", (uid,))
        rs = cur.fetchall()
        if not rs:
            return "Error"
        else:
            return rs[0][0]

def getIDFromUsername(username):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT uid FROM users WHERE username = ?;", (username,))
        rs = cur.fetchall()
        if not rs:
            return None
        else:
            return rs[0][0]


def get_meetup_info(eid):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM meetups where eid = ?;", [(str(eid))])
        row = cur.fetchone()

        if (not row):
            return None

        mdict = collections.OrderedDict()
        mdict['eid'] = row[0]
        mdict['starttime'] = row[1]
        mdict['endtime'] = row[2]
        mdict['classname'] = row[3]
        mdict['subject'] = row[4]
        mdict['createdby'] = row[5]
        #mdict['coordinator'] = row[6]
        mdict['latitude'] = row[6]
        mdict['longitude'] = row[7]
        return (mdict)

def findByClass(term):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM meetups where classname = '?';", (term,))
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
            #mdict['coordinator'] = row[6]
            mdict['latitude'] = row[6]
            mdict['longitude'] = row[7]

            meetuplist.append(mdict)

        return (meetuplist)

def confirmUserPass(user,passw):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT password FROM users where username = ?;", (user,))
        row = cur.fetchall()

        if not row:
            return False
<<<<<<< HEAD

        return True


=======
#        (str(user) == row[0] and str(passw) == row[1]):
#            return True
#        else:
        return True
>>>>>>> d4a223147f7ee1be26c5e234a4631b40889fb299
        # def exists_user():
        # def delete_meetup():
        # def delete_user():
