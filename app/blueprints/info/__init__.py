from flask import Blueprint

bp = Blueprint('about_us', __name__, url_prefix='/about_us')

from . import routes