from flask import *
from flask_wtf import Form 
from wtforms import TextField,TextAreaField,validators,StringField,SubmitField
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'development key'
#Model
class ReviewInputForm(Form):

	fname = TextField("First Name: ",validators=[validators.Required("Please enter your name.")])
	product = TextField("Product Name: ",validators=[validators.Required("Please enter the product name.")])
	review = TextField("Review: ",validators=[validators.Required("Please provide the review.")])
	submit = SubmitField("Submit")


#view
@app.route('/',methods = ['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/addreview',methods = ['GET', 'POST'])
def addreview():
	form = ReviewInputForm(request.form)
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('reviewform.html', form = form)
		else:
			msg = ""
			try:
				fname = form.fname.data
				product = form.product.data
				review = form.review.data

				with sql.connect('database.db') as con:
					cur = con.cursor()
					cur.execute("INSERT INTO REVIEWS(name,product,review) VALUES(?,?,?)",(fname,product,review))
					con.commit()
					msg = "Review added succesfully!  Thank You for Reviewing."
			except:
				con.rollback()
				msg = "Error occured! Please try after some time."

			return render_template('result.html', msg = msg)


	elif request.method == 'GET':
		return render_template('reviewform.html', form = form)

@app.route('/display')
def display():
	con = sql.connect('database.db')
	con.row_factory = sql.Row 
	cur = con.cursor()
	cur.execute("SELECT * FROM REVIEWS")
	rows = cur.fetchall()
	return render_template("reviews.html",rows = rows)



if __name__ == '__main__':
   app.run(debug = True)