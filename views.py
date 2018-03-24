from flask import render_template


def hello_world():
    return render_template('welcome_page.html', name_from_python='\"Hello, world!\"')
