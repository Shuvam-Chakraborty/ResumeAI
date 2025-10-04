import json
import os
from typing import Dict, List

STORAGE_DIR = "user_data"

def ensure_storage_dir():
    """Create storage directory if it doesn't exist"""
    os.makedirs(STORAGE_DIR, exist_ok=True)

def get_user_file_path(user_id: str) -> str:
    """Get file path for user's resume data"""
    ensure_storage_dir()
    return os.path.join(STORAGE_DIR, f"{user_id}_resumes.json")

def save_user_resumes(user_id: str, resumes: List[Dict]):
    """Save user's resumes to file"""
    file_path = get_user_file_path(user_id)
    with open(file_path, 'w') as f:
        json.dump(resumes, f, indent=2)

def load_user_resumes(user_id: str) -> List[Dict]:
    """Load user's resumes from file"""
    file_path = get_user_file_path(user_id)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []

def delete_user_resume(user_id: str, resume_index: int):
    """Delete a specific resume"""
    resumes = load_user_resumes(user_id)
    if 0 <= resume_index < len(resumes):
        resumes.pop(resume_index)
        save_user_resumes(user_id, resumes)