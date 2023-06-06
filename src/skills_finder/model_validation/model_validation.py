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
        if extracted_text:
            valid_tokens = [word for word in extracted_text if word in trained_model.key_to_index]
            logging.info("Task: Validating Tokens: (model_validation) executed")

            if valid_tokens:
                avg_vector = sum(trained_model.get_vector(word) for word in valid_tokens) / len(valid_tokens)
                similar_words = trained_model.similar_by_vector(avg_vector)
                logging.info("Task: Calculating Similarity Score: (model_validation) executed")

                extracted_skills = []
                logging.info("Task: Appending Similar Words to extracted_skills: (model_validation) executed")

                for word, similarity in similar_words:
                    if similarity >= 0.2:
                        extracted_skills.append(word)
                return extracted_skills, 200

            else:
                return "No valid tokens found in the vocabulary.", 204
        else:
            return "No input received from file", 204

    except ValueError:
        logging.debug("Some Error Occured: (model_validation)")
        raise ValueError
