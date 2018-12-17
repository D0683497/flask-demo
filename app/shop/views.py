from flask import render_template
from . import shop

@shop.route('/')
def index():
    return render_template('shop/index.html')