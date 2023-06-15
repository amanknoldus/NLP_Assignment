import logging

import pandas as pd
from src.utils.constants import file_path
from src.utils.helpers import configuration

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def model_validation(trained_model, extracted_text):
    """
    getting the word vector and checking for similarity and returning the word
    who have similarity of one
    @return extracted skills
    @param extracted_text
    @param trained_model
    """
    data = pd.read_csv(file_path)
    skill_corpus = data['skill_set_encode'].tolist()

    expanded_tokens = extracted_text
    word_vectors = trained_model
    similar_words = []
    for word in expanded_tokens:
        for skill_word in skill_corpus:
            try:
                vec1 = word_vectors.wv[word]
                vec2 = word_vectors.wv[skill_word]
                word_set = set(vec1)
                skill_word_set = set(vec2)
                intersection = len(word_set.intersection(skill_word_set))
                union = len(word_set.union(skill_word_set))
                jaccard_similarity = intersection / union
                if jaccard_similarity >= configuration.threshold:
                    similar_words.append(word)
            except KeyError:
                logging.debug("Some Error Occured: (model_validation)")
                pass

    unique_values = set(similar_words)
    skills_extracted = []
    for value in unique_values:
        skills_extracted.append(value)

    if len(skills_extracted) > 0:
        return skills_extracted, 200
    else:
        return "No skills found", 202

