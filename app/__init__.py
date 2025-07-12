from flask import Flask
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "..", "templates"))
    app.config.from_pyfile("config.py")  # ← 後ほどDB設定などを追加

    from app.routes import main
    app.register_blueprint(main)

    return app