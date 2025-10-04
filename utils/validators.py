import re

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """Validate phone format"""
    cleaned = re.sub(r'[^\d]', '', phone)
    return len(cleaned) >= 10

def validate_resume_data(data: dict) -> tuple[bool, list]:
    """Validate resume data and return (is_valid, errors)"""
    errors = []
    
    if not data.get('name', '').strip():
        errors.append("Name is required")
    
    if data.get('email') and not validate_email(data['email']):
        errors.append("Invalid email format")
    
    if data.get('phone') and not validate_phone(data['phone']):
        errors.append("Invalid phone format")
    
    if not data.get('experiences'):
        errors.append("At least one experience is required")
    
    if not data.get('education'):
        errors.append("At least one education entry is required")
    
    return len(errors) == 0, errors