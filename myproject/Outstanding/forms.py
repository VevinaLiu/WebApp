from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField



class grouping(FlaskForm):
    claimquery = RadioField('Query Methods', choices=[
        ('bdate','By Date'), ('bgroup','By Supplier')], default='bdate')
    submit = SubmitField('Submit')
