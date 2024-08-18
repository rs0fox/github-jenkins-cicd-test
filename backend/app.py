from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/games', methods=['GET'])
def get_games():
    games = [
        {"id": 1, "title": "Game One", "genre": "RPG"},
        {"id": 2, "title": "Game Two", "genre": "Action"},
    ]
    return jsonify(games)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
