import logging

import pandas as pd
from src.utils.constants import file_path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def expanding_tokens(text):
    expanded_tokens = []
    for i, token in enumerate(text):
        expanded_tokens.append(token)
        if i < len(text) - 1:
            expanded_tokens.append(' '.join([token, text[i + 1]]))
    return expanded_tokens


def model_validation(trained_model, extracted_text):
    """
    getting the word vector and checking for similarity and returning the word
    who have similarity of one
    @return extracted skills
    @param extracted_text
    @param trained_model
    """
    data = pd.read_csv(file_path)
    skill_corpus = data['skill_set'].tolist()
    expanded_tokens = expanding_tokens(extracted_text)
    word_vectors = trained_model
    similar_words = []
    for word in expanded_tokens:
        for skill_word in skill_corpus:
            try:
                vec1 = word_vectors[word]
                vec2 = word_vectors[skill_word]
                word_set = set(vec1)
                skill_word_set = set(vec2)
                intersection = len(word_set.intersection(skill_word_set))
                union = len(word_set.union(skill_word_set))
                jaccard_similarity = intersection / union
                if jaccard_similarity >= 0.5:
                    similar_words.append(word)
            except ValueError:
                logging.debug("Some Error Occured: (model_validation)")
                raise ValueError

    unique_values = set(similar_words)
    for value in unique_values:
        return value
