from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField

from wtforms.validators import DataRequired, Email

class OrderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phone_num = StringField('Phone Number', validators=[DataRequired()])
    msg = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField()
