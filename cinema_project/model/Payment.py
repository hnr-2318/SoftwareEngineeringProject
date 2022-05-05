from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed


class Payment(FlaskForm):
    paymentSubmit = SubmitField(label = "Continue to Checkout")