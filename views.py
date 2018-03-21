from flask import render_template


def hello_world():
    return render_template('welcome_page.html', text='Hello, world')
