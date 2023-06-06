import logging
import pickle

from gensim.models import Word2Vec
import pandas as pd
from src.utils.constants import file_path, saved_model

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


def get_model_training():
    """
    Function to receive get request from server and start training of model
    @return: Response Message
    """
    try:
        trained_model = model_training()
        pickle.dump(trained_model, open(saved_model / "sill_extract.pkl", 'wb'))
        return "Model Trained Successfully", 200

    except Exception as e:
        return str(e)
