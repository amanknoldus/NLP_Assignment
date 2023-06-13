from gensim.models import Word2Vec
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from src.utils.constants import file_path


def model_training():
    """
    getting the resume text and training it
    @return word vectors
    """
    data = pd.read_csv(file_path)
    sentences = data['skill_set'].tolist()

    tokenized_sentences = [sentence.split() for sentence in sentences]
    print(tokenized_sentences)
    model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)
    word_vectors = model.wv
    return word_vectors
