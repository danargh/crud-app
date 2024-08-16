import bcrypt
from flask import Flask
import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.config.config import Config
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

# loading env variabel
load_dotenv()

# declaring flask app
app = Flask(__name__)

# calling the dev config
config = Config().dev_config

# make app use env
app.env = config.ENV

# load secret key defined in the .env file
app.secret_key = os.environ.get("SECRET_KEY")
bcrypt = Bcrypt(app)

# path for sqllite database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")

# To specify to track modifications of objects and emit signals
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get(
    "SQLALCHEMY_TRACK_MODIFICATIONS"
)

# sql achemy instance
db = SQLAlchemy(app)

# flask migrate instance handle migrations
migrate = Migrate(app, db)

# import api blueprint to register it with app
from src.routes import api

app.register_blueprint(api, url_prefix="/api")

# import models to let the migrate tool know
from src.models.user_model import User
