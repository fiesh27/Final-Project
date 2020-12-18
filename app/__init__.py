from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    with app.app_context():
        from app.blueprints.intro import bp as intro
        app.register_blueprint(intro)

        from app.blueprints.order import bp as order
        app.register_blueprint(order)
        
        from app.blueprints.gallery import bp as gallery
        app.register_blueprint(gallery)
        
        from app.blueprints.info import bp as info
        app.register_blueprint(info)
        from . import routes


        
    return app

