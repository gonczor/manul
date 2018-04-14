from flask import render_template, redirect, url_for, request, abort
from flask_login import login_required, logout_user


def hello_world():
    return render_template('welcome_page.html', name_from_python='\"Hello, world!\"')


def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        abort(400)


def logout():
    logout_user()
    return redirect(url_for('hello_world'))


@login_required
def admin_panel():
    return render_template('admin_panel.html')
