from flask_wtf import FlaskForm
from wtforms import SubmitField

class dltemp(FlaskForm):
    submit1 = SubmitField('Download Template')
    submit2 = SubmitField('Process Rebate')