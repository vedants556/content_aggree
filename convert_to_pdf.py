import markdown2
from weasyprint import HTML
from datetime import datetime
import os

def convert_markdown_to_pdf():
    today_str = datetime.today().strftime("%Y-%m-%d")
    md_filename = f"digest-{today_str}.md"
    pdf_filename = f"digest-{today_str}.pdf"

    if not os.path.exists(md_filename):
        print(f"❌ Markdown file not found: {md_filename}")
        return

    with open(md_filename, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_content = markdown2.markdown(md_content)
    HTML(string=html_content).write_pdf(pdf_filename)

    print(f"✅ PDF file saved: {pdf_filename}")

if __name__ == "__main__":
    convert_markdown_to_pdf()

