from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class totquery(FlaskForm):
    code = StringField('Please enter supplier code')
    submit1 = SubmitField('Submit')