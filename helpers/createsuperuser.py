from sys import exit
from getpass import getpass

from db import db
from db.models import User
from main import create_app
from utils.hash import hash_password


def execute():
    create_app()

    username = input('Give username: ')
    password = getpass('Give password: ')
    password = hash_password(password)
    password_confirmation = getpass('Confirm password: ')
    password_confirmation = hash_password(password_confirmation)

    if password != password_confirmation:
        print('Passwords do not match')
        exit(1)

    admin = User(username=username, password=password, is_admin=True)
    db.session.add(admin)
    db.session.commit()

    # Check
    user = User.query.filter(User.username == username).first()
    if user:
        print('Successfully created user: {}'.format(user.username))
    else:
        print('User not created.')
