import PyPDF2
import textract
from PIL import Image
import pytesseract


def extract_text_from_pdf(resume):
    text_data = ''
    pdf_reader = PyPDF2.PdfReader(resume)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text_data += page.extract_text()
    return text_data


def extract_text_from_word(resume):
    text_data = textract.process(resume)
    return text_data


def extract_text_from_image(resume):
    image = Image.open(resume)
    text_data = pytesseract.image_to_string(image)
    return text_data
