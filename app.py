from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from assessment_app.config import Config
from assessment_app import create_app, db
from assessment_app.models import User, Module, Assessment, Question, AnswerOption, Result
from .routes import auth, admin, user

app = Flask(__name__)
app.config.from_object(Config)
app = create_app()

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect unauthorized users to login page

# Register blueprints (to be created)
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(user)

if __name__ == "__main__":
    app.run(debug=True)