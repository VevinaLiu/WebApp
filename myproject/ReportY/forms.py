from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

class batches(FlaskForm):
    batchno = SelectField('Please select a batch',
                          choices=[('BATCH1', 'BATCH1'), ('BATCH2', 'BATCH2'), ('BATCH3', 'BATCH3'),
                                   ('BATCH4', 'BATCH4'), ('BATCH5', 'BATCH5'), ('BATCH6', 'BATCH6')],
                          default='BATCH1')
    submit = SubmitField('Download Report')