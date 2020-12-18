from flask import Blueprint

bp = Blueprint('gallery', __name__, url_prefix='/gallery')

from . import routes