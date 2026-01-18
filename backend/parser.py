import pdfplumber
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(path):
    text = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"
            else:
                img = page.to_image(resolution=300).original
                ocr_text = pytesseract.image_to_string(img)
                text += ocr_text + "\n"

    return text


def load_resumes_from_folder(folder):
    resumes = {}

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            path = os.path.join(folder, file)
            resumes[file] = extract_text_from_pdf(path)

    return resumes
