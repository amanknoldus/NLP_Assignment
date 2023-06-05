import logging
from gensim.models import Word2Vec
import pandas as pd
from src.utils.constants import file_path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def model_training():
    """
    getting the resume text and training it
    @return word vectors
    """
    try:
        data = pd.read_csv(file_path)
        sentences = data['skill_set'].tolist()

        tokenized_sentences = [sentence.split() for sentence in sentences]

        model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)
        word_vectors = model.wv
        logging.info("Task: Training Model: (model_training) executed")
        return word_vectors

    except Exception as e:
        logging.debug("Some Error Occured: (model_training)")
        return str(e)
