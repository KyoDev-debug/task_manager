import os
from flask import Flask

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "..", "templates"))
    app.config.from_pyfile("config.py")

    from app.routes import main
    app.register_blueprint(main)

    return app