from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from .tictactoe.tictactoe_ai import where, checkGrid, computer_play, computer_play_easy, computer_play_medium

ttt = Blueprint('ttt', __name__)
cors = CORS()

@ttt.route('check', methods=['POST'])
@cross_origin()
def check():
    grid = [[request.get_json()[str(i) + str(j)] for j in range(3)] for i in range(3)]
    winner = {
        'who': checkGrid(grid),
        'where': where(grid)
    }
    return jsonify(winner)

@ttt.route('hard', methods=['POST'])
@cross_origin()
def next_move():
    grid = [[request.get_json()[str(i) + str(j)] for j in range(3)] for i in range(3)]
    return jsonify(computer_play(grid))

@ttt.route('easy', methods=['POST'])
@cross_origin()
def next_easy_move():
    grid = [[request.get_json()[str(i) + str(j)] for j in range(3)] for i in range(3)]
    return jsonify(computer_play_easy(grid))

@ttt.route('normal', methods=['POST'])
@cross_origin()
def next_medium_move():
    grid = [[request.get_json()[str(i) + str(j)] for j in range(3)] for i in range(3)]
    return jsonify(computer_play_medium(grid))