import io
from weasyprint import HTML, CSS

def generate_pdf(html_content: str) -> bytes:
    """Generate PDF from HTML content with proper margins"""
    try:
        # Updated CSS to match the template's padding exactly
        pdf_css = CSS(string="""
            @page {
                size: A4;
                margin: 45px 65px;
            }
            body {
                margin: 0;
                padding: 0;
            }
            .resume-container {
                padding: 0 !important;
                margin: 0 !important;
            }
            .resume-page {
                padding: 0 !important;
                margin: 0 !important;
                box-shadow: none !important;
            }
        """)
        
        buf = io.BytesIO()
        HTML(string=html_content).write_pdf(target=buf, stylesheets=[pdf_css])
        buf.seek(0)
        return buf.getvalue()
        
    except Exception as e:
        raise Exception(f"PDF generation failed: {str(e)}")