from flask import Flask, render_template, jsonify, request
import chess

from eval import evaluate_board

app = Flask(__name__)
game = chess.Board()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/next_move', methods=['POST'])
def next_move():
    game_state = request.get_json()

    game.set_fen(game_state['fen'])
    move = evaluate_board(game)

    game.push(move)
    return jsonify({'fen': game.fen()})


if __name__ == "__main__":
    app.run(debug=True)