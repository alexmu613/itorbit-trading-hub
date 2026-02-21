from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

auth bp = Blueprint('auth', __name__)

# Mock database (replace with real database)
users = {} # This will be a dictionary where key is username and value is password hash

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'User already exists.'}), 409

    users[username] = generate_password_hash(password)
    return jsonify({'message': 'User registered successfully.'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_password_hash = users.get(username)

    if not user_password_hash or not check_password_hash(user_password_hash, password):
        return jsonify({'message': 'Invalid credentials.'}), 401

    return jsonify({'message': 'Login successful.'}), 200
