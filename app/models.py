from app import db
from datetime import datetime

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
