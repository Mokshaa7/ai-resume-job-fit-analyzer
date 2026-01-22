import pdfplumber
import pytesseract
from PIL import Image
import os
import shutil

def configure_tesseract():
    # If running on Windows (local machine)
    if os.name == "nt":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    else:
        # Linux / Docker environment
        tesseract_path = shutil.which("tesseract")
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path

configure_tesseract()


def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # If text found, return it
    if text.strip():
        return text.strip()

    # OCR fallback (safe)
    try:
        from PIL import Image

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                img = page.to_image(resolution=300).original
                text += pytesseract.image_to_string(img)

        return text.strip()

    except Exception as e:
        print("OCR failed:", e)
        return ""


def load_resumes_from_folder(folder):
    resumes = {}

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            path = os.path.join(folder, file)
            resumes[file] = extract_text_from_pdf(path)

    return resumes
