from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


class LoginForm(FlaskForm):
    Username = StringField(
        'Username',
        validators=[InputRequired(message='不能為空!')],
        render_kw={'class': 'form-control', 'placeholder': 'Username'}
    )
    Password = PasswordField(
        'Password',
        validators=[InputRequired(message='不能為空!')],
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
    Email = StringField('Email address',
                        validators=[InputRequired(
                            message='不能為空!'), Email(message='格式錯誤!')],
                        render_kw={'class': 'form-control',
                                   'placeholder': 'Email address'}
                        )
    Username = StringField(
        'Username',
        validators=[InputRequired(message='不能為空!')],
        render_kw={'class': 'form-control', 'placeholder': 'Username'}
    )
    Password = PasswordField(
        'Password',
        validators=[InputRequired(message='不能為空!'), EqualTo(
            'ConfirmPassword', message='您輸入的密碼不相同!')],
        render_kw={'class': 'form-control', 'placeholder': 'Password'}
    )
    ConfirmPassword = PasswordField(
        'Confirm Password',
        validators=[InputRequired(message='不能為空!')],
        render_kw={'class': 'form-control', 'placeholder': 'Confirm Password'}
    )
    regist = SubmitField(
        '註冊',
        render_kw={'class': 'btn btn-lg btn-primary btn-block'}
    )
