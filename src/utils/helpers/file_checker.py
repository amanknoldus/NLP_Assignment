import logging
import magic
import mimetypes
import imghdr
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

word_log = "Task: is_word_document executed successfully: (is_word_document)"
image_log = "Task: image_checker executed successfully: (image_checker)"


def is_pdf(file_path):
    try:
        logging.info("Task: Check For Pdf File: (is_pdf) executed")
        file_type = magic.from_file(file_path, mime=True)
        file_extension = mimetypes.guess_extension(file_type)

        if file_extension == '.pdf':
            logging.info("File is pdf format: (is_pdf)")
            logging.info("Task: is_pdf executed successfully: (is_pdf)")
            return True
        else:
            logging.info("File is not pdf format: (is_pdf)")
            logging.info("Task: is_pdf executed successfully: (is_pdf)")
            return False

    except ValueError:
        logging.info("Task: is_pdf exception occured: (is_pdf)")
        raise ValueError


def is_word_document(file_path):
    try:
        file_type = magic.from_file(file_path, mime=True)

        if file_type == 'application/msword':
            logging.info("Task: Check For Word File Type A: (is_word_document) executed")
            logging.info(word_log)
            return True
        elif file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            logging.info("Task: Check For Word File Type B: (is_word_document) executed")
            logging.info(word_log)
            return True
        else:
            logging.info("File is not word document format: (is_word_document)")
            logging.info(word_log)
            return False

    except ValueError:
        logging.info("Task: is_word_document exception occured: (is_word_document)")
        raise ValueError


def image_checker(file_path):
    try:
        image_format = imghdr.what(file_path)
        logging.info("Task: Check For Image File: (image_checker) executed")
        if image_format is not None:
            logging.info("File is image format: (is_word_document)")
            logging.info(image_log)
            return True
        else:
            logging.info("File is not image format: (is_word_document)")
            logging.info(image_log)
            return False

    except ValueError:
        logging.info("Task: image_checker exception occured: (image_checker)")
        raise ValueError
