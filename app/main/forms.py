from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class EditProfileForm(FlaskForm):
    name = StringField('Real name', render_kw={'class': 'form-control'})
    location = StringField('Location', render_kw={'class': 'form-control'})
    about = TextAreaField('About me', render_kw={'class': 'form-control', 'placeholder': 'About me'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-lg btn-primary btn-block'})