import logging

from gensim.models import Word2Vec
import pandas as pd

from src.utils.constants import file_path


def model_training():
    """
    getting the resume text and training it
    @return word vectors
    """
    try:

        data = pd.read_csv(file_path)
        skill_corpus = data['skill_set'].tolist()
        model = Word2Vec()
        model.build_vocab([skill_corpus], update=True)
        model.train([skill_corpus], total_examples=len(skill_corpus), epochs=model.epochs)
        logging.info("Task: Training Model: (model_training) executed")
        return model

    except Exception as e:
        logging.debug("Some Error Occured: (model_training)")
        return str(e)


