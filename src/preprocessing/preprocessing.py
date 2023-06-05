import pytesseract
from pdf2image import convert_from_path
from src.utils.constants import resume_path, stopwords
from src.utils.helpers.pdf_checker import is_pdf
from PIL import Image
import re
from nltk.tokenize import word_tokenize


class PreProcessing:

    def __init__(self, filename):
        self.filename = filename

    def extract_text(self):
        """
        Function to extract text data from input file: (pdf,png or jpg)
        """
        file_name = self.filename
        resume = resume_path / file_name

        if is_pdf(resume):
            converted_pdf_resume = self.pdf_to_image(resume)
            text_data = pytesseract.image_to_string(converted_pdf_resume)
            cleaned_data = self.clean_text_data(text_data)
            tokenized_data = self.tokenize_data(cleaned_data)
            return tokenized_data

        else:
            image = Image.open(resume)
            text_data = pytesseract.image_to_string(image)
            cleaned_data = self.clean_text_data(text_data)
            tokenized_data = self.tokenize_data(cleaned_data)
            print(tokenized_data)
            return tokenized_data

    @staticmethod
    def pdf_to_image(resume):
        """
        Function to convert given input pdf into image
        @param resume: input pdf file
        @return: image file
        """
        images = convert_from_path(resume)
        for i, image in enumerate(images):
            return image

    @staticmethod
    def clean_text_data(text_data):
        """
        Function to clean textual data by remove unnecessary
        symbols, extra spaces, tags.
        @param text_data: raw text data
        @return: preprocessed data
        """
        removed_symbols = re.sub('[^a-zA-Z]', ' ', str(text_data))
        removed_extra_spaces = re.sub(' +', ' ', removed_symbols)
        removed_tags = re.sub(r'\b(ha)+\b', '', removed_extra_spaces)
        replaced_newline_tag = removed_tags.replace('\n', ' ')
        return replaced_newline_tag.lower().strip()

    @staticmethod
    def tokenize_data(cleaned_data):
        """
        Function to tokenize textual data and remove stopwords from it.
        @param cleaned_data:
        @return: tokenized and removed stopwords data
        """
        tokens = word_tokenize(cleaned_data)
        filtered_tokens = [word for word in tokens if word.lower() not in stopwords]
        return filtered_tokens
