from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField,SubmitField,BooleanField


from wtforms.validators import DataRequired, length, Email,equal_to


class RegistrationForm(FlaskForm):
    userName = StringField("UserName", validators=[DataRequired(), length(min=2, max=20)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password" , validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),equal_to("password")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password" , validators=[DataRequired()])
    remember = BooleanField("Stay Logged In")
    submit = SubmitField("Sign in")