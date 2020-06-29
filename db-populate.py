#imserting data into the database
import sqlite3
db_locale='users.db' #flask will create this db if it doesn't exist

connie=sqlite3.connect(db_locale)
c=connie.cursor() #used to create commands

#populating the table involves INSERTING data into the database....
#this will be done via the online form - but we can add some initial data.

c.execute("""

INSERT INTO comments (title,name,comments) VALUES 
('But what is meaning?', 'Mrs Marvin', 'First, we need to ask the question: What does the term meaning, mean?'),
('42','Joe Bloggs','Yeah. Someone was going to say 42. A cliche. Hope someone else says something more intriguing')
	""")

connie.commit()
connie.close()
