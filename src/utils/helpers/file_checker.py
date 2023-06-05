import os
import magic
from PIL import Image


def is_pdf(file_path):
    mime = magic.from_file(file_path, mime=True)
    return mime == 'application/pdf'


def word_checker(file_path):
    filename, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in ['.doc', '.docx']


def image_checker(file_path):
    Image.open(file_path)
    return True
