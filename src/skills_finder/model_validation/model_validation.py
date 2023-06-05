import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def model_validation(trained_model, extracted_text):
    """
    getting the word vector and checking for similarity and returning the word
    who have similarity of one
    @return extracted skills
    @param extracted_text:
    @param trained_model:
    """
    try:
        word_vectors = trained_model
        extracted_data = extracted_text

        valid_tokens = [word for word in extracted_data if word in word_vectors.key_to_index]
        logging.info("Task: Validating Tokens: (model_validation) executed")

        if valid_tokens:
            avg_vector = sum(word_vectors.get_vector(word) for word in valid_tokens) / len(valid_tokens)
            similar_words = word_vectors.similar_by_vector(avg_vector)
            logging.info("Task: Calculating Similarity Score: (model_validation) executed")

            extracted_skills = []

            for word, similarity in similar_words:
                if similarity >= 0.2:
                    extracted_skills.append(word)
                    logging.info("Task: Appending Similar Words to extracted_skills: (model_validation) executed")
            return extracted_skills

        else:
            return "No valid tokens found in the vocabulary."

    except Exception as e:
        logging.debug("Some Error Occured: (model_validation)")
        return str(e)

