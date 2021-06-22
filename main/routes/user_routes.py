from flask import jsonify, request
from app import app
from main.services.user import User


@app.route("/")
def index():
    return '''Index'''


# curl -i -H "Content-Type:application/json" -H "Accept: application/json" http://localhost:5000/user/id
@app.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    user = User.get_user_by_id(id)

    return jsonify(user.to_json())

