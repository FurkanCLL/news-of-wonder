from flask import Blueprint, render_template
from app.models import Post

main = Blueprint('main', __name__)

@main.route('/')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@main.route('/post/<int:post_id>')
def post_detail(post_id):
    from flask import abort
    post = Post.query.get(post_id)
    if not post:
        abort(404)
    return render_template("post_detail.html", post=post)