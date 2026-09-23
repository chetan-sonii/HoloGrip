import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-change-me')
    APP_URL = os.getenv('APP_URL', '').rstrip('/')
    SELF_PING_INTERVAL = int(os.getenv('SELF_PING_INTERVAL', '10'))
