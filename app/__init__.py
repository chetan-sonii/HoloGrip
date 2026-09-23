from flask import Flask, render_template

from config import Config
from app.routes.main import main_bp
from app.routes.api import api_bp
from app.routes.health import health_bp
from app.services.keep_alive import start_keep_alive


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_class)

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(health_bp)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html", active_page=None), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/500.html", active_page=None), 500

    start_keep_alive(app)
    return app
