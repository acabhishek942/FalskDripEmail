from wtforms import (Form, BooleanField, StringField, PasswordField, validators,
                    IntegerField, TextAreaField, RadioField)
from flask_ckeditor import CKEditorField


class DripEmailBasicDetailsForm(Form):
  title  = StringField('Title')
  receiverList = StringField('receiverList', [validators.Length(min=5)]) # comma seperated values without spaces
  noOfStages = IntegerField('stages')
  frequency = RadioField('frequency', choices = [
    ('fibonacci', 'fibonacci'),
   ('alternate start with next odd day', 'alternate start with next odd day'),
   ('alternate start with next even day', 'alternate start with next even day')])

class DripEmailTemplateForm(Form):
  subject = StringField('subject')
  emailTemplate = CKEditorField('template')
