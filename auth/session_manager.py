import streamlit as st
import json
from datetime import datetime

def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        'authenticated': False,
        'user_id': None,
        'username': None,
        'page': 'home',  # home, single_resume, multiple_resume
        'current_resume': None,
        'resume_list': [],
        'selected_template': 'ats_friendly',
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def is_authenticated():
    return st.session_state.get('authenticated', False)

def login_user(username, user_id):
    st.session_state.authenticated = True
    st.session_state.username = username
    st.session_state.user_id = user_id

def logout_user():
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.user_id = None
    st.session_state.page = 'home'

def get_user_data_key():
    """Get localStorage-like key for current user"""
    return f"resume_data_{st.session_state.user_id}"