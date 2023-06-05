from flask import Flask, request, jsonify
from src.skills_finder.pipeline.pipeline import ExtractingSkills
from src.utils.constants import resume_path
from pydantic import BaseModel, validator, FilePath

main = Flask(__name__)


class FileInput(BaseModel):
    file_path: FilePath

    @validator('file_path')
    def validate_file(cls, value):
        if value.endswith(('.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx')):
            return value
        else:
            raise ValueError("invalid file type!")


@main.route("/", methods=["POST"])
def get_file():
    """
    Function to get input file: (pdf, images) and pass it for processing phase to extract skill from it.
    @return: skill set
    """
    try:
        response = []
        file_path = request.files['file']

        file_path.save(resume_path / file_path.filename)
        input_file_name = file_path.filename

        process = ExtractingSkills(input_file_name)
        result = process.pipeline()
        response.append(result)
        return jsonify(response)

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    main.run(debug=True)
