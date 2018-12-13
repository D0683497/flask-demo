from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    Username = StringField(
        'Username',
        validators=[DataRequired(message='不能為空!'), ],
        render_kw={'class': 'form-control', 'placeholder': 'Username'}
    )
    Password = PasswordField(
        'Password',
        validators=[DataRequired(message='不能為空!')],
        render_kw={'class': 'form-control', 'placeholder': 'Password'}
    )
    rememberme = BooleanField(
        'Remember me'
    )
    login = SubmitField(
        '登入',
        render_kw={'class': 'btn btn-lg btn-primary btn-block'}
    )


class RegistForm(FlaskForm):
    def validata_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email已被註冊')

    def validata_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('使用者已被註冊')
    Email = StringField('Email address',
                        validators=[DataRequired(
                            message='不能為空!'), Email(message='格式錯誤!'), validata_email],
                        render_kw={'class': 'form-control',
                                   'placeholder': 'Email address'}
                        )
    name = StringField('Real name', 
                        render_kw={'class': 'form-control', 'placeholder': 'Real name'}
                        )
    Username = StringField(
        'Username',
        validators=[DataRequired(message='不能為空!'), validata_username],
        render_kw={'class': 'form-control', 'placeholder': 'Username'}
    )
    Password = PasswordField(
        'Password',
        validators=[DataRequired(message='不能為空!'), 
                    EqualTo('ConfirmPassword', message='您輸入的密碼不相同!')],
        render_kw={'class': 'form-control', 'placeholder': 'Password'}
    )
    ConfirmPassword = PasswordField(
        'Confirm Password',
        validators=[DataRequired(message='不能為空!')],
        render_kw={'class': 'form-control', 'placeholder': 'Confirm Password'}
    )
    about = TextAreaField('About me', 
                            render_kw={'class': 'form-control', 'placeholder': 'About me'}
                        )
    location = StringField('Location', 
                            render_kw={'class': 'form-control', 'placeholder': 'Location'}
                        )
    regist = SubmitField(
        '註冊',
        render_kw={'class': 'btn btn-lg btn-primary btn-block'}
    )


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(
        '目前的密碼', 
        validators=[DataRequired(message='不能為空!')], 
        render_kw={'class': 'form-control', 'placeholder': 'Username'}
    )
    password = PasswordField(
        '新密碼', 
        validators=[DataRequired(message='不能為空!'), 
                    EqualTo('ConfirmPassword', message='您輸入的密碼不相同!')], 
        render_kw={'class': 'form-control', 'placeholder': 'Username'}
    )
    ConfirmPassword = PasswordField(
        '再次輸入新密碼',
        validators=[DataRequired(message='不能為空!')],
        render_kw={'class': 'form-control', 'placeholder': 'Username'}
    )
    submit = SubmitField(
        'Submit',
        render_kw={'class': 'btn btn-lg btn-primary btn-block'}
    )
