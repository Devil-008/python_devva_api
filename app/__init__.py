import os
from flask import Flask, jsonify
from app.extensions import db
from config import config_by_name, Config


def create_app(config_name: str = None) -> Flask:
    """Application factory for Flask REST API."""
    app = Flask(__name__)

    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "default")

    config_class = config_by_name.get(config_name, Config)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Register Blueprints
    from app.routes.users import users_bp
    app.register_blueprint(users_bp)

    # Global Error Handlers for clean JSON API responses
    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({"error": "Bad Request", "message": str(error)}), 400

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not Found", "message": "The requested resource was not found"}), 404

    @app.errorhandler(405)
    def method_not_allowed_error(error):
        return jsonify({"error": "Method Not Allowed", "message": "The method is not allowed for the requested URL"}), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500

    # Auto-create tables in development mode if database tables don't exist
    with app.app_context():
        db.create_all()

    return app
