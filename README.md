# Resume Builder AI

A Streamlit app for generating professional resumes — individually or in bulk — powered by Llama 4 via OpenRouter.

## Features

- **AI Writing** — Generate or improve professional summaries using `meta-llama/llama-4-maverick`
- **Live Preview** — See layout changes instantly as you fill out your resume
- **3 Templates** — ATS Friendly, Modern, and Classic styles
- **Multi-Format Export** — Download as PDF (WeasyPrint) or DOCX (python-docx)
- **Bulk Generation** — Upload an Excel file to generate a ZIP of PDFs for multiple candidates

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

Set your OpenRouter API key in `config/api_config.py`.

To generate sample bulk data for testing:
```bash
python test/excel_generator.py
```

## Project Structure

```
├── app.py                    # Entry point
├── components/               # UI pages (home, login, single/multi resume editor)
├── utils/                    # PDF/DOCX generation, AI calls, Excel parsing
├── templates/                # Jinja2 HTML templates (ats_friendly, modern, classic)
├── config/                   # API config and theme settings
└── auth/                     # Session and credential management
```

## Notes

- Passwords are hashed with SHA-256 and stored in `users_db.json`
- Bulk uploads support up to 5 entries per section per candidate
- Required fields: Name, Experience, Education
