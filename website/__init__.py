from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ASDFEKJBASD123'

    from .views import views
    from .api import api

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

    return app