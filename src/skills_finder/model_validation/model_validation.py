def model_validation(trained_model, extracted_text):
    """
    getting the word vector and checking for similarity and returning the word
    who have similarity of one
    @return extracted skills
    @param extracted_text
    @param trained_model
    """
    word_vectors = trained_model
    extracted_data = extracted_text

    valid_tokens = [word for word in extracted_data if word in word_vectors.key_to_index]
    return valid_tokens
