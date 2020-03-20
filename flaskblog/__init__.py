from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
userpass = 'mysql//root:'
basedir  = '127.0.0.1'
dbname   = '/test'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
db = SQLAlchemy(app)
api = Api(app)

from flaskblog import routes
