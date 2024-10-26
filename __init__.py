from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database and login manager with the app
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Import routes
        from .routes import auth, admin, user
        app.register_blueprint(auth)
        app.register_blueprint(admin)
        app.register_blueprint(user)

    return app