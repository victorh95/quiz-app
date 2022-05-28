from flask import Flask, request

import jwt_utils
import endpoints_functions

app = Flask(__name__)


@app.route('/')
def hello_world():
    x = 'world'
    return f"Hello, {x}"


@app.route('/quiz-info', methods=['GET'])
def get_quiz_infos():
    size, scores = endpoints_functions.get_quiz_infos()
    return {"size": size, "scores": scores}, 200


@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    if payload["password"] == "Vive l'ESIEE !":
        return {"token": jwt_utils.build_token()}, 200
    return "Wrong password", 401


@app.route('/questions', methods=['POST'])
def add_question():
    if not endpoints_functions.verify_token(request):
        return "Unauthorized", 401

    new_question = request.get_json()
    endpoints_functions.add_question(new_question)
    return "New question successfully added", 200


@app.route('/questions/<position>', methods=['DELETE'])
def delete_question(position):
    if not endpoints_functions.verify_token(request):
        return "Unauthorized", 401

    if not endpoints_functions.verify_position(position):
        return "Position not found", 404

    endpoints_functions.delete_question(position)
    return "", 204


@app.route('/questions/<position>', methods=['GET'])
def get_question(position):
    if not endpoints_functions.verify_position(position):
        return "Position not found", 404

    question = endpoints_functions.get_question(position)
    return question, 200


@app.route('/questions/<position>', methods=['PUT'])
def update_question(position):
    if not endpoints_functions.verify_token(request):
        return "Unauthorized", 401

    if not endpoints_functions.verify_position(position):
        return "Position not found", 404

    modified_question = request.get_json()
    endpoints_functions.update_question(position, modified_question)
    return 'Question edited successfully', 200


@app.route('/participations', methods=['POST'])
def add_participations():
    payload = request.get_json()
    try:
        player_name, score = endpoints_functions.add_participations(payload)
    except IndexError:
        return "", 400
    return {
        'playerName': player_name,
        'score': score
    }, 200


@app.route('/participations', methods=['DELETE'])
def delete_participations():
    if not endpoints_functions.verify_token(request):
        return "Unauthorized", 401

    endpoints_functions.delete_participations()
    return "", 204


if __name__ == "__main__":
    app.run(ssl_context='adhoc', use_reloader=True, debug=True)
