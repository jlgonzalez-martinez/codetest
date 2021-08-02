""" Presentation app module """
import logging

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from application.services.pet_service import PetService
from config import settings
from infrastructure.providers.provider_factory import provider_factory
from presentation.rest.management import views as management_views
from presentation.rest.pet import views as pet_views

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)


def start():
    """
    Run Sanic app binding services and blueprints
    """
    LOGGER.info(f'Starting application {settings.app.name}')
    app.register_blueprint(management_views.bp)
    app.register_blueprint(pet_views.bp)
    Swagger(app)
    _init_services()
    app.run(host=settings.app.host, port=settings.app.port, processes=settings.app.workers)


def _init_services():
    """
    Init services needed for the application
    """
    PetService(providers=[provider_factory(dict(provider)) for provider in settings.providers])
