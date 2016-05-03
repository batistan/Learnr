create table users (
   uid integer primary key autoincrement,
   username text not null, 
   password text not null);

create table meetups(
  	eid integer primary key autoincrement,
  	classname text not null,
  	subject text not null,
  	starttime datetime not null,
  	endtime datetime not null,
  	createdby integer not null);

create table RSVPS(
eid integer,
uid integer,
FOREIGN KEY (eid) REFERENCES meetups(eid)
FOREIGN KEY (uid) REFERENCES users(uid)); 