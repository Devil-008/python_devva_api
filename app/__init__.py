from flask import Flask
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import HTTPException
from app.utils.response import api_response
from app.utils.exceptions import BaseAppException

def create_app():
    app = Flask(__name__)

    @app.errorhandler(BaseAppException)
    def handle_app_exception(error):
        return api_response(error.status_code, False, error.message, None)

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return api_response(error.code, False, error.description, None)

    @app.errorhandler(SQLAlchemyError)
    def handle_db_exception(error):
        app.logger.error(f"Database Error: {str(error)}")
        return api_response(500, False, "A database error occurred", None)

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        app.logger.error(f"Unhandled Exception: {str(error)}")
        return api_response(500, False, "An internal server error occurred", None)

    from app.routes.users import users_bp
    app.register_blueprint(users_bp)
    return app