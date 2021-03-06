from flask import current_app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms.validators import DataRequired


class FileUploadForm(FlaskForm):
    user_email = StringField('user email')
    file = FileField('file', validators=[DataRequired()])

    def validate_file(self, field):
        _, ext = field.data.filename.split(".")
        if ext in current_app.config["POSSIBLE_FILE_EXTENSION"]:
            return True

        field.errors.append("txt 형식의 requirements 파일을 업로드해주세요!")
        return False
