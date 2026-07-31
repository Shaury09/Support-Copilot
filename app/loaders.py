from pathlib import Path
from pypdf import PdfReader
from bs4 import BeautifulSoup

def load_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return {
        "text": text,
        "metadata": {
            "source": Path(file_path).name,
            "type": "markdown"
        }
    }


def load_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return {
        "text": text,
        "metadata": {
            "source": Path(file_path).name,
            "type": "pdf"
        }
    }


def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    return {
        "text": soup.get_text(),
        "metadata": {
            "source": Path(file_path).name,
            "type": "html"
        }
    }
