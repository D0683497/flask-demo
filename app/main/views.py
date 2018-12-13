from flask import render_template, abort, flash, redirect, url_for
from . import main
from .. import db
from ..models import User
from flask_login import login_required, current_user
from .forms import EditProfileForm


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about = form.about.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('修改成功', 'success')
        return redirect(url_for('main.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about.data = current_user.about
    return render_template('edit_profile.html', form=form)