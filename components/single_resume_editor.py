import streamlit as st
from utils.resume_renderer import render_resume_html
from utils.pdf_generator import generate_pdf
from utils.docx_generator import generate_docx
from utils.ai_generator import generate_professional_summary, improve_existing_summary
from components.template_selector import render_template_selector
from utils.storage_manager import save_user_resumes, load_user_resumes

def render_single_resume_editor():
    # Simple back button
    if st.button("← Back"):
        if st.session_state.resume_list:
            st.session_state.page = 'multiple_resume'
        else:
            st.session_state.page = 'home'
        st.rerun()
    
    st.title("Resume Editor")
    
    # Template selector
    render_template_selector()
    
    st.markdown("---")
    
    # Two column layout
    left, right = st.columns([1, 1], gap="large")
    
    with left:
        render_editor_form()
    
    with right:
        render_preview_and_download()

def render_editor_form():
    st.header("Edit Resume")
    
    resume = st.session_state.current_resume
    
    # Basic Info
    with st.expander("Basic Information", expanded=True):
        name = st.text_input("Full Name", resume.get('name', ''), key='input_name')
        email = st.text_input("Email", resume.get('email', ''), key='input_email')
        phone = st.text_input("Phone", resume.get('phone', ''), key='input_phone')
        location = st.text_input("Location", resume.get('location', ''), key='input_location')
        linkedin = st.text_input("LinkedIn", resume.get('linkedin', ''), key='input_linkedin')
        github = st.text_input("GitHub (optional)", resume.get('github', ''), key='input_github')

        resume.update({
            'name': name,
            'email': email,
            'phone': phone,
            'location': location,
            'linkedin': linkedin,
            'github': github
        })

        resume.setdefault('basics', {})
        resume['basics'].update({
            'name': name,
            'email': email,
            'phone': phone,
            'location': location,
            'linkedin': linkedin,
            'github': github
        })

    # Professional Summary with AI Generation
    with st.expander("Professional Summary", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✨ Generate with AI", use_container_width=True):
                with st.spinner("Generating..."):
                    generated_summary = generate_professional_summary(resume)
                    if generated_summary:
                        resume['summary'] = generated_summary
                        resume.setdefault('basics', {}).update({'summary': generated_summary})
                        st.rerun()
        
        with col2:
            if st.button("🔄 Improve Current", use_container_width=True, 
                        disabled=not resume.get('summary', '').strip()):
                with st.spinner("Improving..."):
                    current = resume.get('summary', '')
                    improved_summary = improve_existing_summary(current, resume)
                    if improved_summary:
                        resume['summary'] = improved_summary
                        resume.setdefault('basics', {}).update({'summary': improved_summary})
                        st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        summary = st.text_area(
            "Summary", 
            resume.get('summary', ''), 
            height=120,
            help="Use AI to generate or write your own professional summary"
        )
        resume['summary'] = summary
        resume.setdefault('basics', {}).update({'summary': summary})

    # Experience Section
    render_experience_section(resume)
    
    # Projects Section
    render_projects_section(resume)
    
    # Education Section
    render_education_section(resume)
    
    # Skills
    with st.expander("Skills"):
        skills = st.text_area(
            "Skills (one category per line)", 
            resume.get('skills', ''), 
            height=100,
            help="Example: Leadership: Speaking, Fundraising, Communication"
        )
        resume['skills'] = skills
        resume.setdefault('basics', {}).update({'skills': skills})
    
    st.session_state.current_resume = resume


def render_experience_section(resume):
    with st.expander("Professional Experience"):
        if 'experiences' not in resume:
            resume['experiences'] = []
        
        for i, exp in enumerate(resume['experiences']):
            st.markdown(f"**Experience {i+1}**")
            
            col1, col2 = st.columns([5, 1])
            with col1:
                exp['role'] = st.text_input("Job Title", exp.get('role', ''), key=f"exp_role_{i}")
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("×", key=f"remove_exp_{i}", use_container_width=True):
                    resume['experiences'].pop(i)
                    st.rerun()
            
            exp['company'] = st.text_input("Company", exp.get('company', ''), key=f"exp_company_{i}")
            
            col_loc, col_dur = st.columns(2)
            with col_loc:
                exp['location'] = st.text_input("Location", exp.get('location', ''), key=f"exp_loc_{i}")
            with col_dur:
                exp['duration'] = st.text_input("Duration", exp.get('duration', ''), key=f"exp_dur_{i}")
            
            if 'details' not in exp:
                exp['details'] = []
            
            for j, detail in enumerate(exp['details']):
                col_d, col_r = st.columns([5, 1])
                with col_d:
                    exp['details'][j] = st.text_area("Detail", detail, key=f"exp_detail_{i}_{j}", height=60)
                with col_r:
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("×", key=f"remove_detail_{i}_{j}"):
                        exp['details'].pop(j)
                        st.rerun()
            
            if st.button("+ Add Detail", key=f"add_exp_detail_{i}"):
                exp['details'].append("")
                st.rerun()
            
            st.markdown("---")
        
        if st.button("+ Add Experience", use_container_width=True):
            resume['experiences'].append({
                'role': '', 'company': '', 'location': '', 'duration': '', 'details': ['']
            })
            st.rerun()

def render_projects_section(resume):
    with st.expander("Projects (Optional)"):
        if 'projects' not in resume:
            resume['projects'] = []
        
        for i, proj in enumerate(resume['projects']):
            st.markdown(f"**Project {i+1}**")
            
            col1, col2 = st.columns([5, 1])
            with col1:
                proj['name'] = st.text_input("Project Name", proj.get('name', ''), key=f"proj_name_{i}")
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("×", key=f"remove_proj_{i}", use_container_width=True):
                    resume['projects'].pop(i)
                    st.rerun()
            
            col_tech, col_dur = st.columns(2)
            with col_tech:
                proj['technologies'] = st.text_input("Technologies", proj.get('technologies', ''), key=f"proj_tech_{i}")
            with col_dur:
                proj['duration'] = st.text_input("Duration", proj.get('duration', ''), key=f"proj_dur_{i}")
            
            if 'details' not in proj:
                proj['details'] = []
            
            for j, detail in enumerate(proj['details']):
                col_d, col_r = st.columns([5, 1])
                with col_d:
                    proj['details'][j] = st.text_area("Detail", detail, key=f"proj_detail_{i}_{j}", height=60)
                with col_r:
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("×", key=f"remove_proj_detail_{i}_{j}"):
                        proj['details'].pop(j)
                        st.rerun()
            
            if st.button("+ Add Detail", key=f"add_proj_detail_{i}"):
                proj['details'].append("")
                st.rerun()
            
            st.markdown("---")
        
        if st.button("+ Add Project", use_container_width=True):
            resume['projects'].append({
                'name': '', 'technologies': '', 'duration': '', 'details': ['']
            })
            st.rerun()

def render_education_section(resume):
    with st.expander("Education"):
        if 'education' not in resume:
            resume['education'] = []
        
        for i, edu in enumerate(resume['education']):
            st.markdown(f"**Education {i+1}**")
            
            col1, col2 = st.columns([5, 1])
            with col1:
                edu['degree'] = st.text_input("Degree", edu.get('degree', ''), key=f"edu_degree_{i}")
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("×", key=f"remove_edu_{i}", use_container_width=True):
                    resume['education'].pop(i)
                    st.rerun()
            
            edu['school'] = st.text_input("School", edu.get('school', ''), key=f"edu_school_{i}")
            
            col_det, col_year = st.columns(2)
            with col_det:
                edu['details'] = st.text_input("Details (optional)", edu.get('details', ''), key=f"edu_details_{i}")
            with col_year:
                edu['year'] = st.text_input("Year", edu.get('year', ''), key=f"edu_year_{i}")
            
            st.markdown("---")
        
        if st.button("+ Add Education", use_container_width=True):
            resume['education'].append({'degree': '', 'school': '', 'details': '', 'year': ''})
            st.rerun()

def render_preview_and_download():
    st.header("Preview")
    
    resume = st.session_state.current_resume
    template = st.session_state.selected_template
    
    zoom = st.slider("Zoom", 50, 150, 80, step=10)
    scale = zoom / 100
    
    try:
        html = render_resume_html(resume, template)
        
        preview_html = f"""
        <div style="width: 100%; height: 700px; background: #e5e5e5; overflow: auto; border: 2px solid #ccc; border-radius: 4px;">
            <div style="transform: scale({scale}); transform-origin: 0 0; margin: 20px; background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: inline-block;">
                {html}
            </div>
        </div>
        """
        
        st.components.v1.html(preview_html, height=720, scrolling=False)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Download buttons
        col1, col2 = st.columns(2)
        
        with col1:
            pdf_bytes = generate_pdf(html)
            st.download_button(
                "📄 Download PDF",
                pdf_bytes,
                f"{resume.get('name', 'resume').replace(' ', '_')}.pdf",
                "application/pdf",
                use_container_width=True
            )
        
        with col2:
            docx_bytes = generate_docx(resume)
            st.download_button(
                "📝 Download DOCX",
                docx_bytes,
                f"{resume.get('name', 'resume').replace(' ', '_')}.docx",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
    
    except Exception as e:
        st.error(f"Error rendering resume: {str(e)}")