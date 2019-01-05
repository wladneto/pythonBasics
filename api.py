from flask import Flask, jsonify, abort

app = Flask(__name__)
users = [
    {
        "id": 1,
        "nome": "Fulano",
        "idade": 30
    },
    {
        "id": 2,
        "nome": "Ciclano",
        "idade": 40
    }
]

@app.route('/users/api/1.0/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/users/api/1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [u for u in users if u["id"] == user_id]
    if len(user) == 0:
        return abort(404)
    return jsonify({"user": user[0]})