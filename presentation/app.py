""" Presentation app module """
import logging

from flask import Flask
from flasgger import Swagger


from config import settings
from presentation.rest.management import views as management_views

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)


def start():
    """
    Run Sanic app binding services and blueprints
    """
    LOGGER.info(f'Starting application {settings.app.name}')
    app.register_blueprint(management_views.bp)
    Swagger(app)
    app.run(host=settings.app.host, port=settings.app.port, processes=settings.app.workers)
