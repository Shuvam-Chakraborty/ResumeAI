import streamlit as st
import hashlib
import json
import os

# Simple file-based user storage (simulates localStorage)
USER_DB_FILE = "users_db.json"

def load_users():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DB_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup_user(username, email, password):
    users = load_users()
    
    if username in users:
        return False, "Username already exists"
    
    user_id = hashlib.md5(username.encode()).hexdigest()
    users[username] = {
        'user_id': user_id,
        'email': email,
        'password': hash_password(password)
    }
    
    save_users(users)
    return True, user_id

def login_user_auth(username, password):
    users = load_users()
    
    if username not in users:
        return False, None, "User not found"
    
    if users[username]['password'] != hash_password(password):
        return False, None, "Incorrect password"
    
    return True, users[username]['user_id'], "Success"