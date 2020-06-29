#extract data from the database
import sqlite3
db_locale='users.db' #flask will create this db if it doesn't exist

connie=sqlite3.connect(db_locale)
c=connie.cursor() #used to create commands

c.execute("""

SELECT * from comments

	""")

user_info=c.fetchall() 
for user in user_info:
	print(user)


connie.commit()
connie.close()

