from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login/")
def login():
    return render_template('login.html')


@app.route("/regist/")
def regist():
    return render_template('regist.html')


if __name__ == '__main__':
    app.run(debug=True)
