import PyPDF2
import textract
from PIL import Image
import pytesseract
import pdfplumber


def extract_text_from_pdf(resume):
    text_data = ''
    with pdfplumber.open(resume) as pdf:
        for page in pdf.pages:
            text_data += page.extract_text()

    return text_data


def extract_text_from_word(resume):
    text_data = textract.process(resume)
    return text_data


def extract_text_from_image(resume):
    image = Image.open(resume)
    text_data = pytesseract.image_to_string(image)
    return text_data
