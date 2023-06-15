import os

import nltk

from src.utils.constants import resume_path, stopwords
from src.utils.helpers.data_extraction import extract_text_from_pdf, extract_text_from_word, extract_text_from_image
from src.utils.helpers.file_checker import is_pdf, image_checker, is_word_document
import re
import logging
from nltk.tokenize import word_tokenize

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PreProcessing:

    def __init__(self, filename):
        self.filename = filename

    def extract_text(self):
        """
        Function to extract text data from input file: (pdf,word or image)
        @return: extracted skills array
        """
        try:
            file_name = self.filename
            resume = resume_path / file_name
            logging.info("Task: Setting Resume File Name: (extract_text) executed")

            if is_pdf(resume):
                logging.info("Task: Entered into Text Data From Pdf: (extract_text) executed")

                text_data = extract_text_from_pdf(resume)
                cleaned_data = self.clean_text_data(text_data)
                tokenized_data = self.tokenize_data(cleaned_data)
                removed_stopwords = self.remove_stopwords(tokenized_data)
                re_tokenized_data = self.tokenize_data(removed_stopwords)
                expanded_text = self.expand_tokens(re_tokenized_data)
                logging.info("Task: Exited Text Data From PDF: (extract_text) executed")
                return expanded_text

            elif is_word_document(resume):
                logging.info("Task: Entered into Text Data From Word: (extract_text) executed")

                text_data = extract_text_from_word(resume)
                cleaned_data = self.clean_text_data(text_data)
                tokenized_data = self.tokenize_data(cleaned_data)
                removed_stopwords = self.remove_stopwords(tokenized_data)
                re_tokenized_data = self.tokenize_data(removed_stopwords)
                expanded_text = self.expand_tokens(re_tokenized_data)

                logging.info("Task: Exited Text Data From Word: (extract_text) executed")
                return expanded_text

            elif image_checker(resume):
                logging.info("Task: Entered into Text Data From Image: (extract_text) executed")
                text_data = extract_text_from_image(resume)
                cleaned_data = self.clean_text_data(text_data)
                tokenized_data = self.tokenize_data(cleaned_data)
                removed_stopwords = self.remove_stopwords(tokenized_data)
                re_tokenized_data = self.tokenize_data(removed_stopwords)
                expanded_text = self.expand_tokens(re_tokenized_data)

                logging.info("Task: Exited from Text Data From Image: (extract_text) executed")
                return expanded_text

            else:
                os.remove(resume)
                logging.info("Invalid file format received as Input: (extract_text)")
                raise ValueError

        except ValueError:
            logging.debug("Some Error Occured: (extract_text)")
            raise ValueError("Invalid File Format Provided!")

    @staticmethod
    def clean_text_data(text_data):
        """
        Function to clean textual data by remove unnecessary
        symbols, extra spaces, tags.
        @param text_data: raw text data
        @return: preprocessed data
        """
        try:
            removed_symbols = re.sub('[^a-zA-Z]', ' ', str(text_data))
            logging.info("Task: Removing Symbols: (clean_text_data) executed")

            removed_extra_spaces = re.sub(' +', ' ', removed_symbols)
            logging.info("Task: Removing Extra Spaces: (clean_text_data) executed")

            removed_tags = re.sub(r'\b(ha)+\b', '', removed_extra_spaces)
            logging.info("Task: Removing Tags Spaces: (clean_text_data) executed")

            replaced_newline_tag = removed_tags.replace('\n', ' ')
            logging.info("Task: Replacing new line tags: (clean_text_data) executed")

            return replaced_newline_tag.lower().strip()

        except ValueError:
            logging.debug("Some Error Occured: (clean_text_data)")
            raise ValueError

    @staticmethod
    def tokenize_data(cleaned_data):
        """
        Function to tokenize textual data and remove stopwords from it.
        @param cleaned_data:
        @return: tokenized and removed stopwords data
        """
        try:
            test_tokens = word_tokenize(cleaned_data)
            logging.info("Task: Tokenizing Text Data: (tokenize_data) executed")
            return test_tokens

        except ValueError:
            logging.debug("Some Error Occured: (tokenize_data)")
            raise ValueError

    @staticmethod
    def remove_stopwords(tokenized_data):
        try:
            filtered_tokens = [word for word in tokenized_data if word.lower() not in stopwords]
            stop_words_removed = ' '.join(filtered_tokens)

            logging.info("Task: Remove Stopwords from Text Data: (tokenize_data) executed")
            return stop_words_removed

        except ValueError:
            raise ValueError

    @staticmethod
    def expand_tokens(test_tokens):
        """
        Function to expand text to combined with previous and next word.
        @param test_tokens: tokenized text
        @return: expanded text
        """
        try:
            expanded_tokens = []
            for i, token in enumerate(test_tokens):
                expanded_tokens.append(token)
                if i < len(test_tokens) - 1:
                    expanded_tokens.append('_'.join([token, test_tokens[i + 1]]))

            return expanded_tokens

        except RuntimeError:
            raise ValueError
