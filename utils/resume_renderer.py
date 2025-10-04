from jinja2 import Environment, FileSystemLoader
from config.settings import TEMPLATES

def render_resume_html(resume_data: dict, template_name: str = 'ats_friendly') -> str:
    """Render resume data into HTML using selected template"""
    
    # Get template config
    template_config = TEMPLATES.get(template_name, TEMPLATES['ats_friendly'])
    
    # Setup Jinja environment
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(f'{template_name}.html')
    
    # Merge template config with resume data
    render_data = {**resume_data, **template_config}
    
    return template.render(**render_data)