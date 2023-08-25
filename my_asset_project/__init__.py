from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL
# import os
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

#########################################
###########DATABASE SETUP################
#########################################
# basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql123@localhost/ams_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Migrate(app,db)


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'mysql@123'
# app.config['MYSQL_DB'] = 'ams_flask'
 
# mysql = MySQL(app)
###################################################################
#Login Configs
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


from my_asset_project.core.views import core
from my_asset_project.users.views import users
from my_asset_project.assets.views import add_new_asset
from my_asset_project.assets.views import asset_upload
from my_asset_project.assets.views import asset_search
from my_asset_project.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(add_new_asset)
app.register_blueprint(asset_upload)
app.register_blueprint(asset_search)
app.register_blueprint(error_pages)



