from flask import render_template, redirect, url_for, request, abort
from flask_login import login_required, logout_user, login_user

from utils.password import check_user_password


def hello_world():
    return render_template('welcome_page.html', name_from_python='\"Hello, world!\"')


def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        match, user = check_user_password(request.form['username'], request.form['password'])
        if match:
            login_user(user)
            return redirect(url_for('admin_panel'))
        else:
            return abort(401)
    else:
        return abort(400)


def logout():
    logout_user()
    return redirect(url_for('hello_world'))


@login_required
def admin_panel():
    return render_template('admin_panel.html')
