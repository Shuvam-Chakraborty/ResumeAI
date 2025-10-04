import streamlit as st
from auth.auth_manager import signup_user, login_user_auth
from auth.session_manager import login_user

def render_login_page():
    st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>Resume Builder AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; margin-bottom: 40px;'>Build professional resumes with AI assistance</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submit = st.form_submit_button("Login", use_container_width=True, type="primary")
                
                if submit:
                    if not username or not password:
                        st.error("Please fill all fields")
                    else:
                        success, user_id, message = login_user_auth(username, password)
                        if success:
                            login_user(username, user_id)
                            st.success("Login successful!")
                            st.rerun()
                        else:
                            st.error(message)
        
        with tab2:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.form("signup_form"):
                new_username = st.text_input("Username")
                new_email = st.text_input("Email")
                new_password = st.text_input("Password", type="password")
                confirm_password = st.text_input("Confirm Password", type="password")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submit = st.form_submit_button("Sign Up", use_container_width=True, type="primary")
                
                if submit:
                    if not all([new_username, new_email, new_password, confirm_password]):
                        st.error("Please fill all fields")
                    elif new_password != confirm_password:
                        st.error("Passwords don't match")
                    elif len(new_password) < 6:
                        st.error("Password must be at least 6 characters")
                    else:
                        success, result = signup_user(new_username, new_email, new_password)
                        if success:
                            st.success("Account created! Please login.")
                        else:
                            st.error(result)