from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False, default="article")
    title = db.Column(db.String(150), nullable=False)
    subtitle = db.Column(db.String(300))
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50))

    def __repr__(self):
        return f"<Post {self.title}>"

class AdminUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)