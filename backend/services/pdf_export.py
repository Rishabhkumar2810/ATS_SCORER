import io
import logging
from xhtml2pdf import pisa

logger = logging.getLogger("ats_resume_scorer")


def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:
    pdf_buffer = io.BytesIO()

    combined_html = """
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
    """

    first = True
    for _, html in html_docs.items():
        if not first:
            combined_html += '<div style="page-break-before: always;"></div>'
        combined_html += html
        first = False

    combined_html += """
    </body>
    </html>
    """

    pisa_status = pisa.CreatePDF(
        combined_html,
        dest=pdf_buffer,
        encoding="UTF-8"
    )

    if pisa_status.err:
        raise Exception("Failed to generate PDF")

    return pdf_buffer.getvalue()