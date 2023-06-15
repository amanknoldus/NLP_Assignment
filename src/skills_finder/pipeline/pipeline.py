from src.preprocessing.preprocessing import PreProcessing
from src.skills_finder.model_validation.model_validation import model_validation
import logging
import pickle

from src.utils.constants import model_location

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

skill_finer_model = pickle.load(open(model_location, 'rb'))


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

            if extract_data:
                extracted_text = extract_data.extract_text()
                extracted_skills, response_msg = model_validation(skill_finer_model, extracted_text)
                print(extracted_skills)
                logging.info("Task: Returning Extracted Skills From Resume: (pipeline) executed")
                return extracted_skills, response_msg
            else:
                raise ValueError

        except ValueError:
            logging.debug("Some Error Occured: (pipeline)")
            raise ValueError("No text input received from preprocessing")


