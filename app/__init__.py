from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")  # ← 次の段階でDB設定などを読み込み

    from app.routes import main
    app.register_blueprint(main)

    return app