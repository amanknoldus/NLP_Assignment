from flask import Flask, request, jsonify
from src.skills_finder.model_training.model_training import get_model_training
from src.skills_finder.pipeline.pipeline import ExtractingSkills
from src.utils.constants import resume_path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

main = Flask(__name__)


@main.get("/")
def get_model():
    """
    Function to trigger training of model
    @return:  Response Message
    """
    try:
        result, response_msg = get_model_training()
        return result, response_msg

    except Exception as e:
        return str(e)


@main.route("/", methods=["POST"])
def get_file():
    """
    Function to get input file: (pdf, images, word document) and pass it for processing phase to extract skill from it.
    @return: skill set
    """
    try:
        logging.info("Task: Enter into extracting skills from file: (get_file) executed")
        response = []
        file_path = request.files['file']

        file_path.save(resume_path / file_path.filename)
        input_file_name = file_path.filename

        process = ExtractingSkills(input_file_name)
        result, response_msg = process.pipeline()
        response.append(result)
        logging.info("Task: Returning extracted skills from file: (get_file) executed")
        return jsonify(response), response_msg

    except ValueError:
        logging.debug("Some Error Occured: (get_file)")
        return str(ValueError('Invalid File Format!')),


if __name__ == '__main__':
    main.run(debug=True)
