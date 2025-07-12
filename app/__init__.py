import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # テンプレートフォルダの絶対パスを指定
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))
    app = Flask(__name__, template_folder=template_dir)

    app.config.from_object('app.config.Config')
    db.init_app(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app