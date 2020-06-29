import sqlite3
db_locale='users.db' #flask will create this db if it doesn't exist

connie=sqlite3.connect(db_locale)
c=connie.cursor() #used to create commands

#populating the table involves INSERTING data into the database....
#this will be done via the online form - but we can add some initial data.

c.execute("""

CREATE TABLE comments
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT,
	name TEXT,
	comments TEXT
)

	""")

connie.commit()
connie.close()
