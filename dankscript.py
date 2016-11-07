from datetime import datetime
import string


for i in range(4000):
	name = "Matt"
	year = 1979
	month = 1
	day = 1
	birthday = datetime(year, month, day)
	print "db.mhass.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birthday.strftime('%Y-%m-%d'))+"\"});"

for i in range(4000):
	name = "Felix"
	year = 1991
	month = 1
	day = 1
	birthday = datetime(year, month, day)
	print "db.mhass.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birthday.strftime('%Y-%m-%d'))+"\"});"

for i in range(1800):
	name = "Dom"
	year = 1985
	month = 1
	day = 1
	birthday = datetime(year, month, day)
	print "db.mhass.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birthday.strftime('%Y-%m-%d'))+"\"});"
	
for i in range(100):
	name = "Tom"
	year = 1985
	month = 1
	day = 1
	birthday = datetime(year, month, day)
	print "db.mhass.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birthday.strftime('%Y-%m-%d'))+"\"});"
	
for i in range(100):
	name = "Tomato"
	year = 1985
	month = 1
	day = 1
	birthday = datetime(year, month, day)
	print "db.mhass.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birthday.strftime('%Y-%m-%d'))+"\"});"

	
