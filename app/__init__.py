from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import Config

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    with app.app_context():
        from app.routes import initialize_routes
        initialize_routes(api)

    return app
