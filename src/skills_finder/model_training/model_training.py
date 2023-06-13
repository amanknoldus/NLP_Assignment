from gensim.models import Word2Vec
import pandas as pd

from srcutils.constants import file_path


def model_training(resume_text):
    """
    getting the resume text and training it
    :param resume_text
    :return word vectors
    """
    data = pd.read_csv(file_path)
    sentences = data['skill_set'].tolist()

    tokenized_sentences = [sentence.split() for sentence in sentences]

    model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)
    word_vectors = model.wv
    return word_vectors
