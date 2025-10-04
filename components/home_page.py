import streamlit as st
from auth.session_manager import logout_user
from components.single_resume_editor import render_single_resume_editor
from components.multiple_resume_manager import render_multiple_resume_manager

def render_home_page():
    # Header with logout in top right
    col1, col2 = st.columns([6, 1])
    with col1:
        st.title(f"Welcome, {st.session_state.username}!")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Logout", key="logout_btn", use_container_width=True):
            logout_user()
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Route to different pages
    if st.session_state.page == 'single_resume':
        render_single_resume_editor()
    elif st.session_state.page == 'multiple_resume':
        render_multiple_resume_manager()
    else:
        render_home_options()

def render_home_options():
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Custom CSS for cards
    st.markdown("""
        <style>
        .option-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
            transition: transform 0.3s ease;
            margin: 10px;
            min-height: 200px;
        }
        .option-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 32px rgba(0,0,0,0.2);
        }
        .card-title {
            color: white;
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 12px;
        }
        .card-description {
            color: rgba(255,255,255,0.9);
            font-size: 16px;
            margin-bottom: 24px;
        }
        .option-card-2 {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
            transition: transform 0.3s ease;
            margin: 10px;
            min-height: 200px;
        }
        .option-card-2:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 32px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
            <div class="option-card">
                <div class="card-title">📝 Single Resume</div>
                <div class="card-description">Create and edit one professional resume at a time with AI assistance</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Create Single Resume", use_container_width=True, type="primary", key="btn_single"):
            st.session_state.page = 'single_resume'
            st.session_state.current_resume = create_empty_resume()
            st.rerun()
    
    with col2:
        st.markdown("""
            <div class="option-card-2">
                <div class="card-title">📚 Multiple Resumes</div>
                <div class="card-description">Upload Excel and generate multiple resumes in bulk with ease</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Manage Multiple Resumes", use_container_width=True, type="primary", key="btn_multiple"):
            st.session_state.page = 'multiple_resume'
            st.rerun()

def create_empty_resume():
    return {
        "name": "",
        "location": "",
        "email": "",
        "phone": "",
        "linkedin": "",
        "github": "",
        "summary": "",
        "skills": "",
        "experiences": [],
        "consultancy": [],
        "projects": [],
        "education": []
    }