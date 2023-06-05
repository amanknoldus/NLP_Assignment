def model_validation(trained_model, extracted_text):
    """
    getting the word vector and checking for similarity and returning the word
    who have similarity of one
    @return extracted skills
    @param extracted_text:
    @param trained_model:
    """
    word_vectors = trained_model
    extracted_data = extracted_text

    valid_tokens = [word for word in extracted_data if word in word_vectors.key_to_index]
    print(valid_tokens)

    "test_tokens are the test_tokens = test_sentence.split() , test_sentence is the input text"
    if valid_tokens:
        avg_vector = sum(word_vectors.get_vector(word) for word in valid_tokens) / len(valid_tokens)
        similar_words = word_vectors.similar_by_vector(avg_vector)

        extracted_skills = []

        for word, similarity in similar_words:
            if similarity == 0.1:
                extracted_skills.append(word)

        return extracted_skills

    else:
        return "No valid tokens found in the vocabulary."
