import streamlit as st

def render_template_selector():
    templates = {
        'ats_friendly': 'ATS Friendly',
        'modern': 'Modern',
        'classic': 'Classic'
    }
    
    st.selectbox(
        "Select Template",
        options=list(templates.keys()),
        format_func=lambda x: templates[x],
        key='selected_template'
    )