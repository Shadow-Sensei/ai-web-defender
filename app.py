from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager
import logging 
from logging.handlers import RotatingFileHandler
from security import init_soft_rate_limit
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__,template_folder='templates')
    ## logging part start 
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, "app.log")
    handler = RotatingFileHandler(
        "app.log",
        maxBytes=1_000_000,
        backupCount=3
    )
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    ))
    app.logger.addHandler(handler)
      # ---- CRITICAL PART ----
    app.logger.handlers.clear()          # remove Flask defaults
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    # ---- TEST LOG ----
    app.logger.info("EVENT=APP_STARTED")

    # logging part end 

    init_soft_rate_limit(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.//testdb.db'
    app.secret_key = 'SOME KEY'
    db.init_app(app)
    app.logger.info("EVENT=APP_STARTED")


    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    


    from routes import register_routes
    register_routes(app,db)

    migrate = Migrate(app,db)
    return app 

