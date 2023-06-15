import logging
import pickle

from gensim.models import Word2Vec
import pandas as pd
from nltk import word_tokenize

from src.utils.constants import file_path, saved_model


def model_training():
    """
    getting the resume text and training it
    @return word vectors
    """
    try:

        data = pd.read_csv(file_path)
        skill_corpus = data['skill_set_encode'].tolist()
        tokenized_corpus = [word_tokenize(skill) for skill in skill_corpus]

        model = Word2Vec(tokenized_corpus, size=100, window=5, min_count=1, workers=4)

        # vocabulary = set(model.wv.index2word)
        model.build_vocab([skill_corpus], update=True)
        model.train([skill_corpus], total_examples=len(skill_corpus), epochs=model.epochs)

        # vocabulary = set(model.wv.vocab.keys())

        logging.info("Task: Training Model: (model_training) executed")
        return model

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
        pickle.dump(trained_model, open(saved_model / "skill_extract.pkl", 'wb'))
        return "Model Trained Successfully", 200

    except Exception as e:
        return str(e)
