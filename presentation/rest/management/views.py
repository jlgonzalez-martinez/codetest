""" Management views module """
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/management')


@bp.route('/health', methods=['GET'])
def health():
    """
    Health endpoint to check if the application is responding.
    ---
    tags:
      - Management
    responses:
      200:
        description: The application is up and responding
    """
    return '', 200
