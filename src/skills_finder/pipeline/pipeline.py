from src.preprocessing.preprocessing import PreProcessing
from src.skills_finder.model_training.model_training import model_training
from src.skills_finder.model_validation.model_validation import model_validation


class ExtractingSkills:
    def __init__(self, filename):
        """
        getting data from preprocessing function and calculating the accuracy of k-means
        @param filename: input file name
        """
        self.filename = filename

    def pipeline(self):
        """
        getting the dataframe and calling all the steps in building the model
        @return: accuracy
        """
        file_name = self.filename
        extract_data = PreProcessing(file_name)

        extracted_text = extract_data.extract_text()
        trained_model = model_training()
        extracted_skills = model_validation(trained_model, extracted_text)
        return extracted_skills
