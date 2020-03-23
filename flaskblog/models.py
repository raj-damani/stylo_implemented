from datetime import datetime
from flaskblog import db



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
