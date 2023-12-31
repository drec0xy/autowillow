"""App entry point."""
"""Initialize Flask app."""
import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    mail = Mail(app)

    api = Api(app=app)

    from users.routes import create_authentication_routes

    create_authentication_routes(api=api)

    db.init_app(app)

    with app.app_context():

        db.create_all()  # Create database tables for our data models

        return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)