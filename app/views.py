from flask import render_template
from flask_login import login_required


def hello_world():
    return render_template('welcome_page.html', name_from_python='\"Hello, world!\"')


def login():
    return render_template('login.html')


@login_required
def admin_panel():
    return render_template('admin_panel.html')
