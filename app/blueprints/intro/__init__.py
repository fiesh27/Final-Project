from flask import Blueprint

bp = Blueprint('intro', __name__, url_prefix='/intro')

from . import routes

