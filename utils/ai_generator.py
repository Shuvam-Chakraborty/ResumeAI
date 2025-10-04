import requests
import streamlit as st
from config.api_config import LLAMA_API_KEY, LLAMA_API_URL, LLAMA_MODEL, API_TIMEOUT, MAX_TOKENS, TEMPERATURE

def generate_professional_summary(resume_data: dict) -> str:
    """
    Generate a professional summary using Llama API based on resume data
    
    Args:
        resume_data: Dictionary containing resume information
        
    Returns:
        Generated professional summary text
    """
    try:
        # Build context from resume data
        context = build_resume_context(resume_data)
        
        # Create prompt
        prompt = f"""Based on the following professional information, write a compelling professional summary for a resume. 
The summary should be 3-4 sentences, highlight key strengths and experiences, and be written in first person.

Professional Information:
{context}

Professional Summary:"""

        # API request headers
        headers = {
            "Authorization": f"Bearer {LLAMA_API_KEY}",
            "Content-Type": "application/json",
        }
        
        # API request payload
        payload = {
            "model": LLAMA_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": MAX_TOKENS,
            "temperature": TEMPERATURE
        }
        
        # Make API request
        response = requests.post(
            LLAMA_API_URL,
            headers=headers,
            json=payload,
            timeout=API_TIMEOUT
        )
        
        response.raise_for_status()
        
        # Extract generated text
        result = response.json()
        summary = result['choices'][0]['message']['content'].strip()
        
        return summary
        
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {str(e)}")
        return ""
    except KeyError as e:
        st.error(f"Unexpected API response format: {str(e)}")
        return ""
    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")
        return ""


def build_resume_context(resume_data: dict) -> str:
    """Build context string from resume data for AI generation"""
    context_parts = []
    
    # Add name
    if resume_data.get('name'):
        context_parts.append(f"Name: {resume_data['name']}")
    
    # Add experiences
    if resume_data.get('experiences'):
        context_parts.append("\nWork Experience:")
        for exp in resume_data['experiences'][:3]:  # Limit to top 3 experiences
            if exp.get('role') and exp.get('company'):
                context_parts.append(f"- {exp['role']} at {exp['company']}")
                if exp.get('duration'):
                    context_parts.append(f"  Duration: {exp['duration']}")
    
    # Add projects
    if resume_data.get('projects'):
        context_parts.append("\nKey Projects:")
        for proj in resume_data['projects'][:2]:  # Limit to top 2 projects
            if proj.get('name'):
                context_parts.append(f"- {proj['name']}")
                if proj.get('technologies'):
                    context_parts.append(f"  Technologies: {proj['technologies']}")
    
    # Add education
    if resume_data.get('education'):
        context_parts.append("\nEducation:")
        for edu in resume_data['education']:
            if edu.get('degree') and edu.get('school'):
                context_parts.append(f"- {edu['degree']} from {edu['school']}")
    
    # Add skills
    if resume_data.get('skills'):
        context_parts.append(f"\nSkills: {resume_data['skills'][:200]}")  # Limit skills text
    
    return "\n".join(context_parts)


def improve_existing_summary(current_summary: str, resume_data: dict) -> str:
    """
    Improve an existing summary using AI
    
    Args:
        current_summary: Current summary text
        resume_data: Resume data for context
        
    Returns:
        Improved summary text
    """
    try:
        context = build_resume_context(resume_data)
        
        prompt = f"""Improve the following professional summary to make it more compelling and impactful. 
Keep it 3-4 sentences and maintain a professional tone.

Current Summary:
{current_summary}

Professional Context:
{context}

Improved Summary:"""

        headers = {
            "Authorization": f"Bearer {LLAMA_API_KEY}",
            "Content-Type": "application/json",
        }
        
        payload = {
            "model": LLAMA_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": MAX_TOKENS,
            "temperature": TEMPERATURE
        }
        
        response = requests.post(
            LLAMA_API_URL,
            headers=headers,
            json=payload,
            timeout=API_TIMEOUT
        )
        
        response.raise_for_status()
        result = response.json()
        improved_summary = result['choices'][0]['message']['content'].strip()
        
        return improved_summary
        
    except Exception as e:
        st.error(f"Error improving summary: {str(e)}")
        return current_summary