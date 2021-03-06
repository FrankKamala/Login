from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email
class RegistrationForm(FlaskForm):
    username = StringField('username',
     validators=[DataRequired(),Length(min=2,max =20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])                       
    confirm_password=PasswordField('Confirm',validators=[DataRequired()])