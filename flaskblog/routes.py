from stylometry.classify import *
from stylometry.extract import StyloCorpus
from flask import render_template, url_for, flash, redirect, Flask, request
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import Reviews
from flaskblog import app, db
from flask_restful import Resource, Api
import pandas as pd
api = Api(app)
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",database="test")
mycursor = mydb.cursor()

check_train = False

class TrainData(Resource):
	def get(self):
		mycursor.execute("SELECT full_name,comment FROM  Reviews")
		final_list = []
		for record in mycursor.fetchall():
			author = record[0]
			text = record[1]
			if not text:
				text = ""
			final_list.append({"author": author, "text":text})
		review_corpus = StyloCorpus.get_dictionary_from_db(final_list)
		df = review_corpus.output_dataframe()
		print(type(df))#.to_csv("with_db.csv")
		global dtree
		dtree = StyloDecisionTree(df)
		dtree.fit()
		global check_train
		check_train = True
		return{"check": final_list}

class PredictData(Resource):
	def get(self):
		args = request.args
		reviews = []
		predict_final_list = []
		for key in request.args.to_dict():
			predict_final_list.append({"author":"", "text":request.args.to_dict()[key]})
			reviews.append(request.args.to_dict()[key])
		predict_review_corpus = StyloCorpus.get_dictionary_from_db(predict_final_list)
		predict_df = predict_review_corpus.output_dataframe()
		global dtree
		global check_train
		if not check_train:
			mycursor.execute("SELECT full_name,comment FROM  Reviews")
			final_list = []
			for record in mycursor.fetchall():
				author = record[0]
				text = record[1]
				if not text:
					text = ""
				final_list.append({"author": author, "text":text})
			review_corpus = StyloCorpus.get_dictionary_from_db(final_list)
			df = review_corpus.output_dataframe()
			dtree = StyloDecisionTree(df)
			dtree.fit()
			check_train = True

		return_value = dtree.predict(predict_df)
		data = []
		for i in range(len(reviews)):
			data.append({return_value[i] : reviews[i]})
		return {"data":data}


api.add_resource(TrainData, "/TrainData")
api.add_resource(PredictData, "/PredictData")
"""@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)


"""
