""" Management views module """
import logging
from dataclasses import asdict

from flask import Blueprint, request, jsonify

from application.services.pet_service import PetService

bp = Blueprint('pet', __name__, url_prefix='/pet')
LOGGER = logging.getLogger(__name__)


@bp.route('/', methods=['GET'])
def list_pets():
    """
    List all pets for all providers
    ---
    parameters:
      - in: query
        name: max_results
        schema:
          type: integer
          default: 10
      - in: query
        name: page
        schema:
          type: int
          default: 1
      - in: query
        name: sort_by
        schema:
          type: str
          default: height
      - in: query
        name: desc
        schema:
          type: boolean
          default: false
    responses:
      200:
        description: The application is up and responding
    """
    max_results = int(request.args.get('max_results'))
    page = int(request.args.get('page'))
    start = max_results * (page - 1)
    end = max_results * page
    pets = PetService().get_all(sort_by=request.args.get('sort_by'),
                                descending=request.args.get('desc').lower() == 'True')
    if max_results > len(pets):
        result_pets = jsonify([asdict(pet) for pet in pets])
    elif end >= len(pets):
        result_pets = jsonify([asdict(pet) for pet in pets[start:]])
    else:
        result_pets = jsonify([asdict(pet) for pet in pets[start:end]])
    return result_pets, 200


@bp.route('/<pet_provider>/<pet_id>', methods=['GET'])
def get_pet(pet_provider: str, pet_id: str):
    """
    List all pets for all providers
    ---
    parameters:
      - in: path
        name: pet_provider
        schema:
          type: string
      - in: path
        name: pet_id
        schema:
          type: int
    tags:
      - Pet
    responses:
      200:
        description: The application is up and responding
    """
    pet_id = int(pet_id)
    return jsonify(asdict(PetService().get_by_provider_and_id(pet_id, pet_provider))), 200


