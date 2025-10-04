import streamlit as st
import pandas as pd
from utils.excel_parser import parse_excel_to_resumes
from utils.pdf_generator import generate_pdf
from utils.resume_renderer import render_resume_html
import zipfile
import io

def render_multiple_resume_manager():
    # Simple back button
    if st.button("← Back to Home"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.title("Multiple Resume Manager")
    st.markdown("---")
    
    # Upload Excel
    st.subheader("Upload Excel File")
    uploaded_file = st.file_uploader("Choose Excel file", type=['xlsx', 'xls'], label_visibility="collapsed")
    
    if uploaded_file:
        try:
            resumes = parse_excel_to_resumes(uploaded_file)
            st.session_state.resume_list = resumes
            st.success(f"✓ Loaded {len(resumes)} resumes")
        except Exception as e:
            st.error(f"Error parsing Excel: {str(e)}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display resume list
    if st.session_state.resume_list:
        render_resume_list()

def render_resume_list():
    st.subheader("Resume List")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for i, resume in enumerate(st.session_state.resume_list):
        col1, col2, col3 = st.columns([4, 1, 1])
        
        with col1:
            st.write(f"**{i+1}. {resume.get('name', 'Unnamed')}**")
        
        with col2:
            if st.button("Edit", key=f"edit_{i}", use_container_width=True):
                st.session_state.current_resume = resume
                st.session_state.page = 'single_resume'
                st.rerun()
        
        with col3:
            if st.button("Delete", key=f"delete_{i}", use_container_width=True, type="secondary"):
                st.session_state.resume_list.pop(i)
                st.rerun()
    
    # Download all
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Download All as ZIP", type="primary", use_container_width=True):
        with st.spinner("Creating ZIP file..."):
            zip_buffer = create_zip_of_all_resumes()
            st.download_button(
                "📥 Download ZIP",
                zip_buffer,
                "all_resumes.zip",
                "application/zip",
                use_container_width=True
            )

def create_zip_of_all_resumes():
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for i, resume in enumerate(st.session_state.resume_list):
            html = render_resume_html(resume, st.session_state.selected_template)
            pdf_bytes = generate_pdf(html)
            
            filename = f"{resume.get('name', f'resume_{i+1}')}.pdf"
            zip_file.writestr(filename, pdf_bytes)
    
    zip_buffer.seek(0)
    return zip_buffer.getvalue()