from flask import Flask, render_template, url_for, request, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class LoginForm(FlaskForm):
    Username = StringField(
        'Username', 
        validators=[DataRequired(message='不能為空!')],
        render_kw={'class':'form-control', 'placeholder':'Username'}
    )
    Password = PasswordField(
        'Password',
        validators=[DataRequired(message='不能為空!')],
        render_kw={'class':'form-control', 'placeholder':'Password'}
    )
    login = SubmitField(
        '登入',
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
        print(Username, Password)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route("/regist/")
def regist():
    return render_template('regist.html')


if __name__ == '__main__':
    app.run(debug=True)
