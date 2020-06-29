import sqlite3
db_locale='users.db' #flask will create this db if it doesn't exist

connie=sqlite3.connect(db_locale)
c=connie.cursor() #used to create commands

c.execute("""

DELETE FROM comments

	""")

connie.commit()
connie.close()

