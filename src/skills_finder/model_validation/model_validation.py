def model_validation(resume_text):
    """
    getting the word vector and checking for similarity and returning the word
     who have similarity of one
    :param resume_text
    :return extracted skills
    """
    word_vectors = resume_text[0]

    valid_tokens = [word for word in test_tokens if word in word_vectors.key_to_index]
    "test_tokens are the test_tokens = test_sentence.split() , test_sentence is the input text"
    if valid_tokens:
        avg_vector = sum(word_vectors.get_vector(word) for word in valid_tokens) / len(valid_tokens)
        similar_words = word_vectors.similar_by_vector(avg_vector)
        extracting_skills = []
        for word, similarity in similar_words:
            if similarity == 1.0:
                extracting_skills.append(word)
        return extracting_skills
    else:
        return "No valid tokens found in the vocabulary."
