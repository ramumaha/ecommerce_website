from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='5f5b148e6898f5fc0accdb6c'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
# login_manager=LoginManager(app)
from market import routes




