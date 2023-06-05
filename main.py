import magic
from flask import Flask, request, jsonify
from src.skills_finder.pipeline.pipeline import ExtractingSkills
from src.utils.constants import resume_path

main = Flask(__name__)


def check_file_type(file):
    file_magic = magic.Magic(mime=True)
    file_type = file_magic.from_buffer(file.read())

    allowed_types = ['application/pdf', 'image/']

    if any(file_type.startswith(t) for t in allowed_types):
        return file

    raise ValueError('Invalid File Format!')


@main.route("/", methods=["POST"])
def get_file():
    """
    Function to get input file: (pdf, images) and pass it for processing phase to extract skill from it.
    @return: skill set
    """
    try:
        response = []
        file_path = request.files['file']
        valid_file = check_file_type(file_path)

        if valid_file:
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
