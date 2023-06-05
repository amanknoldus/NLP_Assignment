import magic


def is_pdf(file_path):
    mime = magic.from_file(file_path, mime=True)
    return mime == 'application/pdf'


def word_checker(file_path):
    mime_type = magic.from_file(file_path, mime=True)

    if mime_type == 'application/msword' or mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return True
    else:
        print(f'{file_path.filename} is not a Word document.')


