from flask import Flask
from app.config import Config
from app.api import webscraper_bp
from app.api.flipkart import flipkart_bp
from app_logging import logger
from app.setting import Setting


webscraper_app = Flask(Config.APP_NAME)
webscraper_app.config.from_object(Config)

webscraper_app.register_blueprint(webscraper_bp)
webscraper_app.register_blueprint(flipkart_bp)

if __name__ == "app":
    logger.info(f"[START]: {Config.APP_NAME} running in {Config.ENVIRONMENT} mode in {Setting.PROJECT_BASE_DIR}")
