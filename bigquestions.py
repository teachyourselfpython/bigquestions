#bigquestions.py
from flask import Flask, render_template,url_for,request
import sqlite3

app = Flask(__name__)
db_locale='users.db'



@app.route('/')
@app.route('/home')
def home():
	user_data=query_comments()
	return render_template('home.html',user_data=user_data)

@app.route('/about')
def about():
	return render_template('about.html')

#get post request function
@app.route('/add',methods=['GET','POST'])
def addcomment():
	if request.method=="GET":
		return render_template('addcomment.html')
	else:
		user_details=(
			request.form['title'],
			request.form['name'],
			request.form['comments']

			)
		insertcomment(user_details)
		return render_template('addsuccess.html')


def insertcomment(user_details):
	connie=sqlite3.connect(db_locale)
	c=connie.cursor()
	sql_execute_string='INSERT INTO comments (title,name,comments) VALUES (?,?,?)';
	c.execute(sql_execute_string,user_details)
	connie.commit()
	connie.close()
	print(user_details)


def query_comments():
	connie=sqlite3.connect(db_locale)
	c=connie.cursor()
	c.execute("""
		SELECT * FROM comments		

		""")
	userdata=c.fetchall()
	return userdata




if __name__=='__main__':
	app.run(debug=True)