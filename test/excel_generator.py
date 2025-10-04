import pandas as pd

# Sample data for 3 resumes
data = {
    # Basic Information
    'name': ['John Doe', 'Jane Smith', 'Mike Johnson'],
    'email': ['john.doe@email.com', 'jane.smith@email.com', 'mike.j@email.com'],
    'phone': ['(555) 123-4567', '+1-555-987-6543', '555.111.2222'],
    'location': ['New York, NY', 'San Francisco, CA', 'Austin, TX'],
    'linkedin': ['linkedin.com/in/johndoe', 'linkedin.com/in/janesmith', 'linkedin.com/in/mikej'],
    'github': ['github.com/johndoe', '', 'github.com/mikej'],
    'summary': [
        'Experienced Full Stack Developer with 5+ years building scalable web applications. Passionate about clean code and user experience.',
        'Creative UI/UX Designer with expertise in user research and modern design systems. Led design for 10+ successful product launches.',
        'Data Scientist specializing in machine learning and predictive analytics. Published researcher with 3 years industry experience.'
    ],
    'skills': [
        'Programming: Python, JavaScript, TypeScript, React | Tools: Git, Docker, AWS | Databases: PostgreSQL, MongoDB',
        'Design: Figma, Adobe XD, Sketch | Skills: User Research, Prototyping, Design Systems | Other: HTML/CSS, Basic JavaScript',
        'Languages: Python, R, SQL | ML: TensorFlow, PyTorch, Scikit-learn | Tools: Jupyter, Tableau, Apache Spark'
    ],
    
    # Experience 1
    'experience_1_role': ['Senior Software Engineer', 'Lead UX Designer', 'Data Scientist'],
    'experience_1_company': ['Tech Corp', 'Design Studio Inc', 'Analytics Pro'],
    'experience_1_duration': ['Jan 2021 - Present', 'Mar 2020 - Present', 'Jun 2022 - Present'],
    'experience_1_location': ['New York, NY', 'San Francisco, CA', 'Austin, TX'],
    'experience_1_details': [
        'Led development of microservices architecture serving 1M+ users|Reduced API response time by 60% through optimization|Mentored team of 5 junior developers',
        'Redesigned core product interface increasing user engagement by 45%|Established design system used across 8 product teams|Conducted 50+ user research sessions',
        'Built predictive models achieving 92% accuracy for customer churn|Automated reporting pipeline saving 20 hours per week|Presented insights to C-level executives monthly'
    ],
    
    # Experience 2
    'experience_2_role': ['Software Engineer', 'UX Designer', 'Research Assistant'],
    'experience_2_company': ['StartupXYZ', 'Creative Agency', 'University Lab'],
    'experience_2_duration': ['Jun 2019 - Dec 2020', 'Jan 2018 - Feb 2020', 'Aug 2019 - May 2022'],
    'experience_2_location': ['Remote', 'San Francisco, CA', 'Boston, MA'],
    'experience_2_details': [
        'Developed full-stack features using React and Node.js|Implemented CI/CD pipeline reducing deployment time by 70%|Collaborated with design team on UX improvements',
        'Created wireframes and prototypes for mobile applications|Conducted A/B tests improving conversion rates by 25%|Worked with cross-functional teams of 10+ members',
        'Analyzed large datasets using Python and R|Published 2 papers in peer-reviewed journals|Assisted in grant writing securing $500K in funding'
    ],
    
    # Experience 3
    'experience_3_role': ['Junior Developer', '', ''],
    'experience_3_company': ['Web Solutions LLC', '', ''],
    'experience_3_duration': ['Jan 2018 - May 2019', '', ''],
    'experience_3_location': ['New York, NY', '', ''],
    'experience_3_details': [
        'Built responsive websites using HTML, CSS, and JavaScript|Fixed bugs and implemented new features in legacy codebase|Participated in daily standup and sprint planning',
        '',
        ''
    ],
    
    # Experience 4 & 5 (all empty to show optional nature)
    'experience_4_role': ['', '', ''],
    'experience_4_company': ['', '', ''],
    'experience_4_duration': ['', '', ''],
    'experience_4_location': ['', '', ''],
    'experience_4_details': ['', '', ''],
    'experience_5_role': ['', '', ''],
    'experience_5_company': ['', '', ''],
    'experience_5_duration': ['', '', ''],
    'experience_5_location': ['', '', ''],
    'experience_5_details': ['', '', ''],
    
    # Project 1
    'project_1_name': ['E-Commerce Platform', 'Portfolio Website Builder', 'Customer Segmentation Tool'],
    'project_1_technologies': ['React, Node.js, MongoDB, AWS', 'Figma, Webflow, JavaScript', 'Python, Scikit-learn, Pandas'],
    'project_1_duration': ['6 months', '3 months', '4 months'],
    'project_1_details': [
        'Built scalable e-commerce platform handling 10K daily transactions|Integrated Stripe payment processing and inventory management|Deployed using Docker and AWS ECS',
        'Created drag-and-drop interface for building portfolio sites|Implemented 15+ customizable templates|Achieved 4.8/5 rating from 200+ users',
        'Developed unsupervised learning model for customer clustering|Identified 5 distinct customer segments improving targeting|Created interactive dashboard for business stakeholders'
    ],
    
    # Project 2
    'project_2_name': ['Task Management App', 'Mobile App Redesign', ''],
    'project_2_technologies': ['Vue.js, Firebase, Tailwind CSS', 'Figma, User Testing', ''],
    'project_2_duration': ['4 months', '2 months', ''],
    'project_2_details': [
        'Developed real-time collaborative task management tool|Implemented authentication and role-based access control|Used by 500+ users in beta testing',
        'Redesigned fitness tracking app improving user retention by 35%|Created high-fidelity prototypes tested with 30 users|Documented design decisions in comprehensive style guide',
        ''
    ],
    
    # Project 3, 4, 5 (empty)
    'project_3_name': ['', '', ''],
    'project_3_technologies': ['', '', ''],
    'project_3_duration': ['', '', ''],
    'project_3_details': ['', '', ''],
    'project_4_name': ['', '', ''],
    'project_4_technologies': ['', '', ''],
    'project_4_duration': ['', '', ''],
    'project_4_details': ['', '', ''],
    'project_5_name': ['', '', ''],
    'project_5_technologies': ['', '', ''],
    'project_5_duration': ['', '', ''],
    'project_5_details': ['', '', ''],
    
    # Education 1
    'education_1_degree': ['Bachelor of Science in Computer Science', 'Bachelor of Fine Arts in Design', 'Master of Science in Data Science'],
    'education_1_school': ['MIT', 'Rhode Island School of Design', 'Stanford University'],
    'education_1_year': ['2018', '2018', '2022'],
    'education_1_details': ['GPA: 3.8/4.0, Dean\'s List', 'Summa Cum Laude, Thesis: Modern UI Patterns', 'GPA: 3.9/4.0, Focus: Machine Learning'],
    
    # Education 2
    'education_2_degree': ['', 'Certification in UX Design', 'Bachelor of Science in Statistics'],
    'education_2_school': ['', 'General Assembly', 'University of Texas'],
    'education_2_year': ['', '2019', '2019'],
    'education_2_details': ['', '12-week intensive program', 'GPA: 3.7/4.0, Minor in Mathematics'],
    
    # Education 3, 4, 5 (empty)
    'education_3_degree': ['', '', ''],
    'education_3_school': ['', '', ''],
    'education_3_year': ['', '', ''],
    'education_3_details': ['', '', ''],
    'education_4_degree': ['', '', ''],
    'education_4_school': ['', '', ''],
    'education_4_year': ['', '', ''],
    'education_4_details': ['', '', ''],
    'education_5_degree': ['', '', ''],
    'education_5_school': ['', '', ''],
    'education_5_year': ['', '', ''],
    'education_5_details': ['', '', ''],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = 'sample_resumes.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"✅ Sample Excel file created: {output_file}")
print(f"📊 Contains {len(df)} sample resumes:")
print("   1. John Doe - Software Engineer (3 experiences, 2 projects, 1 education)")
print("   2. Jane Smith - UX Designer (2 experiences, 2 projects, 2 educations)")
print("   3. Mike Johnson - Data Scientist (2 experiences, 1 project, 2 educations)")
print("\n💡 Upload this file to test the Multiple Resume feature!")