from flask import Flask

def create_app():
    app = Flask(__name__)

    from .pirevo import pirevo
    from .tictactop import tictactop

    # enregistrer les blueprint
    app.register_blueprint(pirevo.pirevo, url_prefix='/pirevo/')
    app.register_blueprint(tictactop.ttt, url_prefix='/tictactop/' )

    return app