# 📝 Resume Builder AI

A Streamlit application for creating professional, polished resumes — one at a time or in bulk — with AI-assisted writing and multi-format export.

---

## Features

### Single Resume Editor
- Fill out structured sections: Basic Info, Experience, Projects, Education, and Skills
- **AI Writing Assistant** — click "Generate with AI" to draft a professional summary from scratch, or "Improve Current" to refine what you've already written (powered by `meta-llama/llama-4-maverick` via OpenRouter)
- **Live Preview** — see your resume re-render in real time as you type
- Export as a formatted **PDF** or structured **DOCX** file

### Bulk Resume Generation
- Upload a single Excel file containing data for multiple candidates
- The app parses and maps each row to the internal resume schema
- Generate and download a **ZIP archive** of PDFs for every candidate at once

### Templates
Three visual styles to choose from, each with its own color scheme (configurable in `config/settings.py`):

| Template | Accent Color | Best For |
|---|---|---|
| ATS Friendly | Blue `#2563eb` | Applicant tracking systems |
| Modern | Green `#10b981` | Creative / tech roles |
| Classic | Neutral | Traditional industries |

---

## Tech Stack

| Purpose | Library |
|---|---|
| UI | Streamlit |
| Templating | Jinja2 + HTML/CSS |
| PDF Export | WeasyPrint |
| DOCX Export | python-docx |
| Excel Parsing | Pandas + Openpyxl |
| AI | OpenRouter (Llama 4 Maverick) |

---

## Setup

### Prerequisites
- Python 3.8+
- An [OpenRouter](https://openrouter.ai) API key

### Installation

```bash
git clone https://github.com/your-username/resume-builder-ai.git
cd resume-builder-ai
pip install -r requirements.txt
```

### Configuration

Add your OpenRouter API key in `config/api_config.py`:

```python
OPENROUTER_API_KEY = "your_key_here"
```

### Run

```bash
streamlit run app.py
```

To generate a sample Excel file for testing bulk features:
```bash
python test/excel_generator.py
# Output: test/sample_resumes.xlsx
```

---

## Project Structure

```
├── app.py                         # Entry point and routing
├── components/
│   ├── home_page.py               # Landing page
│   ├── login_page.py              # Auth UI
│   ├── single_resume_editor.py    # Single resume form + preview
│   ├── multiple_resume_manager.py # Bulk upload and export
│   └── template_selector.py      # Template picker UI
├── utils/
│   ├── ai_generator.py            # OpenRouter API calls
│   ├── pdf_generator.py           # WeasyPrint PDF rendering
│   ├── docx_generator.py          # python-docx export
│   ├── excel_parser.py            # Bulk Excel ingestion
│   ├── resume_renderer.py         # Jinja2 HTML rendering
│   ├── storage_manager.py         # user_data/ file persistence
│   └── validators.py              # Field validation (email, phone, required fields)
├── templates/
│   ├── ats_friendly.html
│   ├── modern.html
│   └── classic.html
├── config/
│   ├── api_config.py              # API key, model, timeout settings
│   └── settings.py                # Template colors and app-wide constants
├── auth/
│   ├── auth_manager.py            # Signup/login with SHA-256 hashing
│   └── session_manager.py         # Session state tracking
├── users_db.json                  # Local user credential store
└── test/
    └── excel_generator.py         # Generates sample_resumes.xlsx for testing
```

---

## Validation & Constraints

- **Required fields:** Name, at least one Experience entry, and at least one Education entry
- **Email & phone** are validated against standard formats before export
- **Bulk uploads** support up to 5 entries per section (Experience, Projects, etc.) per candidate
- **AI timeout:** OpenRouter requests cut off after 30 seconds

---

## Authentication

Users sign up and log in via a tabbed interface. Passwords are hashed with **SHA-256** before being written to `users_db.json`. Once authenticated, `session_manager` tracks the active user ID and current page across the app.
