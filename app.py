from flask import Flask, render_template, jsonify, request
import chess

from bots import bot_v7
from engine.move_generator import get_next_move

app = Flask(__name__)
game = chess.Board()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/next_move', methods=['POST'])
def next_move():
    game_state = request.get_json()

    game.set_fen(game_state['fen'])
    move = get_next_move(game, bot_v7)

    game.push(move)
    return jsonify({'fen': game.fen()})


@app.teardown_appcontext
def close_resources(exception):
    pass


if __name__ == "__main__":
    app.run(debug=True)