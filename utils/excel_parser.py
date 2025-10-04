import pandas as pd

def parse_excel_to_resumes(file):
    """
    Parse Excel file to list of resume dictionaries.
    Supports up to 5 entries for each section (experiences, projects, education).
    Only includes entries where at least one field is filled.
    
    Expected columns format:
    Basic: name, email, phone, location, linkedin, github, summary, skills
    Experience: experience_1_role, experience_1_company, experience_1_duration, experience_1_location, experience_1_details
    Projects: project_1_name, project_1_technologies, project_1_duration, project_1_details
    Education: education_1_degree, education_1_school, education_1_year, education_1_details
    """
    df = pd.read_excel(file)
    resumes = []
    
    for _, row in df.iterrows():
        resume = {
            'name': str(row.get('name', '')).strip() if pd.notna(row.get('name')) else '',
            'email': str(row.get('email', '')).strip() if pd.notna(row.get('email')) else '',
            'phone': str(row.get('phone', '')).strip() if pd.notna(row.get('phone')) else '',
            'location': str(row.get('location', '')).strip() if pd.notna(row.get('location')) else '',
            'linkedin': str(row.get('linkedin', '')).strip() if pd.notna(row.get('linkedin')) else '',
            'github': str(row.get('github', '')).strip() if pd.notna(row.get('github')) else '',
            'summary': str(row.get('summary', '')).strip() if pd.notna(row.get('summary')) else '',
            'skills': str(row.get('skills', '')).strip() if pd.notna(row.get('skills')) else '',
            'experiences': [],
            'education': [],
            'projects': []
        }
        
        # Parse experiences (up to 5)
        for i in range(1, 6):
            exp = parse_experience_entry(row, i)
            if exp:  # Only add if at least one field is filled
                resume['experiences'].append(exp)
        
        # Parse projects (up to 5)
        for i in range(1, 6):
            proj = parse_project_entry(row, i)
            if proj:  # Only add if at least one field is filled
                resume['projects'].append(proj)
        
        # Parse education (up to 5)
        for i in range(1, 6):
            edu = parse_education_entry(row, i)
            if edu:  # Only add if at least one field is filled
                resume['education'].append(edu)
        
        resumes.append(resume)
    
    return resumes


def parse_experience_entry(row, index):
    """Parse a single experience entry. Returns None if all fields are empty."""
    role = str(row.get(f'experience_{index}_role', '')).strip() if pd.notna(row.get(f'experience_{index}_role')) else ''
    company = str(row.get(f'experience_{index}_company', '')).strip() if pd.notna(row.get(f'experience_{index}_company')) else ''
    duration = str(row.get(f'experience_{index}_duration', '')).strip() if pd.notna(row.get(f'experience_{index}_duration')) else ''
    location = str(row.get(f'experience_{index}_location', '')).strip() if pd.notna(row.get(f'experience_{index}_location')) else ''
    details_raw = row.get(f'experience_{index}_details', '')
    
    # Check if at least one field is filled
    if not any([role, company, duration, location, details_raw if pd.notna(details_raw) else '']):
        return None
    
    # Parse details (split by | or newline)
    details = []
    if pd.notna(details_raw) and str(details_raw).strip():
        # Split by pipe or newline
        details_str = str(details_raw).strip()
        if '|' in details_str:
            details = [d.strip() for d in details_str.split('|') if d.strip()]
        elif '\n' in details_str:
            details = [d.strip() for d in details_str.split('\n') if d.strip()]
        else:
            details = [details_str] if details_str else []
    
    return {
        'role': role,
        'company': company,
        'duration': duration,
        'location': location,
        'details': details
    }


def parse_project_entry(row, index):
    """Parse a single project entry. Returns None if all fields are empty."""
    name = str(row.get(f'project_{index}_name', '')).strip() if pd.notna(row.get(f'project_{index}_name')) else ''
    technologies = str(row.get(f'project_{index}_technologies', '')).strip() if pd.notna(row.get(f'project_{index}_technologies')) else ''
    duration = str(row.get(f'project_{index}_duration', '')).strip() if pd.notna(row.get(f'project_{index}_duration')) else ''
    details_raw = row.get(f'project_{index}_details', '')
    
    # Check if at least one field is filled
    if not any([name, technologies, duration, details_raw if pd.notna(details_raw) else '']):
        return None
    
    # Parse details
    details = []
    if pd.notna(details_raw) and str(details_raw).strip():
        details_str = str(details_raw).strip()
        if '|' in details_str:
            details = [d.strip() for d in details_str.split('|') if d.strip()]
        elif '\n' in details_str:
            details = [d.strip() for d in details_str.split('\n') if d.strip()]
        else:
            details = [details_str] if details_str else []
    
    return {
        'name': name,
        'technologies': technologies,
        'duration': duration,
        'details': details
    }


def parse_education_entry(row, index):
    """Parse a single education entry. Returns None if all fields are empty."""
    degree = str(row.get(f'education_{index}_degree', '')).strip() if pd.notna(row.get(f'education_{index}_degree')) else ''
    school = str(row.get(f'education_{index}_school', '')).strip() if pd.notna(row.get(f'education_{index}_school')) else ''
    year = str(row.get(f'education_{index}_year', '')).strip() if pd.notna(row.get(f'education_{index}_year')) else ''
    details = str(row.get(f'education_{index}_details', '')).strip() if pd.notna(row.get(f'education_{index}_details')) else ''
    
    # Check if at least one field is filled
    if not any([degree, school, year, details]):
        return None
    
    return {
        'degree': degree,
        'school': school,
        'year': year,
        'details': details
    }