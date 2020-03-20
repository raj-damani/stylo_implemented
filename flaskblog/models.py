from datetime import datetime
from flaskblog import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

class Reviews(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	business_id = db.Column(db.Integer)
	review_id = db.Column(db.Text)
	full_name = db.Column(db.Text)
	avatar = db.Column(db.Text)
	comment = db.Column(db.Text)
	rating = db.Column(db.Integer)
	is_anonymous = db.Column(db.Integer)
	is_flagged = db.Column(db.Integer)
	post_date = db.Column(db.DateTime)
	status = db.Column(db.Text)
	name_check_result = db.Column(db.Text)
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)
