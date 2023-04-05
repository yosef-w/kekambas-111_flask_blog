from . import api
from app.models import Post


@api.route('/')
def index():
    return 'Hello this is the API'

@api.route('/posts')
def get_posts():
    posts = Post.query.all()
    return [post.to_dict() for post in posts]

@api.route('/posts/<post_id>')
def get_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return {'error': f'Post with the ID of {post_id} is not found'}, 404
    return post.to_dict()