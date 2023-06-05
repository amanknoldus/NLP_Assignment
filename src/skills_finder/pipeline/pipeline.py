from src.preprocessing.preprocessing import PreProcessing
from src.skills_finder.model_training.model_training import model_training
from src.skills_finder.model_validation.model_validation import model_validation
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ExtractingSkills:
    def __init__(self, filename):
        """
        getting data from preprocessing function and calculating the accuracy of k-means
        @param filename: input file name
        """
        self.filename = filename
        logging.info("Task: Setting File Name: (ExtractingSkills) executed")

    def pipeline(self):
        """
        getting the dataframe and calling all the steps in building the model
        @return: accuracy
        """
        try:
            file_name = self.filename
            extract_data = PreProcessing(file_name)
            extracted_text = extract_data.extract_text()
            print(extracted_text)
            trained_model = model_training()
            extracted_skills = model_validation(trained_model, extracted_text)
            logging.info("Task: Returning Extracted Skills From Resume: (pipeline) executed")
            return extracted_skills

        except Exception as e:
            logging.debug("Some Error Occured: (pipeline)")
            return str(e)
