from flask import request, jsonify, Blueprint
from flask_cors import CORS, cross_origin
from .market.market import Asset

pirevo = Blueprint('pirevo', __name__)
cors = CORS()

@pirevo.route('risky-asset', methods = ['POST'])
@cross_origin()
def risky_asset_path():
    p, u, d, n = [request.get_json()[c] for c in 'pudn']
    risky_asset = Asset(p, u, d, n)
    S = risky_asset.values
    S_path = risky_asset.generate_path(S)
    
    return jsonify({
        'N': list(range(n+1)),
        'S_path': S_path
    })
    