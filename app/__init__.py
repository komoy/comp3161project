from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from flask_httpauth import HTTPBasicAuth

#from subprocess import call
#call(["mysql-ctl","cli"])

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/mealplanner_recipe_system"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message="You must be logged in to gain access."

app.config.from_object(__name__)
from app import views
