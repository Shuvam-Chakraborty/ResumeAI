import streamlit as st
from auth.session_manager import init_session_state, is_authenticated
from components.login_page import render_login_page
from components.home_page import render_home_page

# Page config - MUST be first
st.set_page_config(
    page_title="Resume Builder AI",
    layout="wide",
    page_icon="📄",
    initial_sidebar_state="collapsed"
)

# Hide the link icon on headers
st.markdown("""
    <style>
    .stTitle a, h1 a, h2 a, h3 a {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session
init_session_state()

# Main routing
def main():
    if not is_authenticated():
        render_login_page()
    else:
        render_home_page()

if __name__ == "__main__":
    main()