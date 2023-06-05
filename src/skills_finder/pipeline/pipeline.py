from src.skills_finder.model_training.model_training import model_training
from src.skills_finder.model_validation.model_validation import model_validation
from src.utils.constants import file_path


class Extracting_Skills:
    def __init__(self):
        """
        getting data from preprocessing function and calculating the accuracy of k-means
         @param dataframe
        @type dataframe
        """
        self.dataset = file_path

    def pipeline(self):
        """
        getting the dataframe and calling all the steps in building the model
        @return: accuracy
        """
        processed_dataframe = pre_processing(self.dataset)
        trained_model = model_training(processed_dataframe)
        extracted_skills = model_validation(trained_model)
        return extracted_skills
