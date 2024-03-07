from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_wtf.file import FileField, FileRequired, FileAllowed
#from wtforms.validators import DataRequired
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])