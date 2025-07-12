import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "your-secret-key"  # 実務では .env に切り出して管理
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, '..', 'task.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False