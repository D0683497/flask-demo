from flask import Flask, render_template, url_for, redirect, flash

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class LoginForm(FlaskForm):
    Username = StringField(
        'Username', 
        validators=[InputRequired(message='不能為空!')],
        render_kw={'class':'form-control', 'placeholder':'Username'}
    )
    Password = PasswordField(
        'Password',
        validators=[InputRequired(message='不能為空!')],
        render_kw={'class':'form-control', 'placeholder':'Password'}
    )
    rememberme = BooleanField(
        'Remember me'
    )
    login = SubmitField(
        '登入',
        render_kw={'class':'btn btn-lg btn-primary btn-block'}
    )

class RegistForm(FlaskForm):
    Email = StringField('Email address',
        validators=[InputRequired(message='不能為空!') ,Email(message='格式錯誤!')],
        render_kw={'class':'form-control', 'placeholder':'Email address'}
    )
    Username = StringField(
        'Username', 
        validators=[InputRequired(message='不能為空!')],
        render_kw={'class':'form-control', 'placeholder':'Username'}
    )
    Password = PasswordField(
        'Password',
        validators=[InputRequired(message='不能為空!'), EqualTo('ConfirmPassword', message='您輸入的密碼不相同!')],
        render_kw={'class':'form-control', 'placeholder':'Password'}
    )
    ConfirmPassword = PasswordField(
        'Confirm Password',
        validators=[InputRequired(message='不能為空!')],
        render_kw={'class':'form-control', 'placeholder':'Confirm Password'}
    )
    regist = SubmitField(
        '註冊',
        render_kw={'class':'btn btn-lg btn-primary btn-block'}
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        Username = form.Username.data
        Password = form.Password.data
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route("/regist/", methods=['GET', 'POST'])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        Email = form.Email.data
        Username = form.Username.data
        Password = form.Password.data
        return redirect(url_for('index'))
    return render_template('regist.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
