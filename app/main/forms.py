from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError
from ..models import Role, User

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed


class EditProfileForm(FlaskForm):
    name = StringField('Real name', render_kw={'class': 'form-control'})
    location = StringField('Location', render_kw={'class': 'form-control'})
    about = TextAreaField('About me', render_kw={'class': 'form-control', 'placeholder': 'About me'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-lg btn-primary btn-block'})


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(),Email()],
                        render_kw={'class': 'form-control', 'placeholder': 'Email'}
                        )
    username = StringField('Username', 
                            validators=[DataRequired()],
                            render_kw={'class': 'form-control', 'placeholder': 'Username'}
                            )
    role = SelectField('Role', 
                        coerce=int,
                        render_kw={'class': 'form-control', 'id': 'inputGroupSelect', 'placeholder': 'Role'}
                        )
    name = StringField('Real name',
                        render_kw={'class': 'form-control', 'placeholder': 'Real name'}
                        )
    location = StringField('Location',
                            render_kw={'class': 'form-control', 'placeholder': 'Location'}
                            )
    about = TextAreaField('About me',
                            render_kw={'class': 'form-control', 'placeholder': 'About me'}
                            )
    submit = SubmitField('Submit',
                        render_kw={'class': 'btn btn-lg btn-primary btn-block'}
                        )

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email 已被使用')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username 已被使用')

class PostForm(FlaskForm):
    body = TextAreaField("分享您的文章", 
                        validators=[DataRequired(message='不能為空!')],
                        render_kw={'class': 'form-control', 'placeholder': '分享您的文章'}
                        )
    photo = FileField("Choose file", validators=[FileAllowed(['jpg', 'png'], '只能是圖片!')], render_kw={'class': 'custom-file-input', 'id': 'customFile'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-lg btn-primary btn-block'})

class CommentForm(FlaskForm):
    body = StringField('寫下您的評論', 
                        validators=[DataRequired()],
                        render_kw={'class': 'form-control', 'placeholder': '分享您的文章'}
                        )
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-lg btn-primary btn-block'})

class DelCommentForm(FlaskForm):
    delete = SubmitField('刪除', render_kw={'class': 'btn btn-outline-danger btn-block'})