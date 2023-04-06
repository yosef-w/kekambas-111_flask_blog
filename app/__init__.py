from flask import Flask
# Import the Config class from the config module that has the app configurations like SECRET_KEY, etc
from config import Config
# Import the classes from Flask-SQLAlchemy and Flask-Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

# Create an instance of SQLAlchemy to connect our app to the database
db = SQLAlchemy(app)
# Create an instance of Migrate that will track our db and app
migrate = Migrate(app, db)

# Create an instance of the LoginManager to set up Authentication
login = LoginManager(app)
# Tell the login manager where to redirect if a user is not logged in
login.login_view = 'login'
# login.login_message = "Hey you can't do that!"
login.login_message_category = 'danger'

# Import the api blueprint and register it with the Flask App
from app.blueprints.api import api
app.register_blueprint(api)


# import all of the routes from the routes file and models from the models file into the current package
from app import routes, models
