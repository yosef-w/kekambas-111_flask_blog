from flask import request
from . import api
from app.models import Post, User


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
        return {'error': f'Post with the ID of {post_id} is not found'}, 400
    return post.to_dict()

# Endpoint to create a new post
@api.route('/posts', methods=["POST"])
def create_post():
    # Check to see that the request body is JSON aka application/json content-type
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    required_fields = ['title', 'body', 'user_id']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            # If the field is not in the request body, add that to missing fields list
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    
    return 'This is the Create Post Route'

@api.route('/signup')
def signup():
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    data = request.json
    required_fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_pass']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    
@api.route('/signup/<user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return {'error': f'{user.id} is not found.'}, 400
    return user.to_user()