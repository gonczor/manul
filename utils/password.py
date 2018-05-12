from hashlib import sha1

from setup import secret_key


def hash_password(unhashed_password):
    # I do not expect password to be given in bytes, but if for any ill reason this happens in future I want
    # to be error-prone.
    if isinstance(unhashed_password, str):
        return sha1(unhashed_password.encode('utf-8') + secret_key).hexdigest()
    else:
        raise TypeError('unhashed_password must be utf-8 string')


def check_user_password(username, password):
    """
    Check if password matches one set for user. Performs hashing.
    :param (str) username:
    :param (str) password: unhashed password
    :return (bool, User): True and user object if user has been found, False and None otherwise.
    """
    from db.models import User
    password = hash_password(password)
    user = User.query.filter(User.username == username).first()
    if user and user.password == password:
        return True, user
    else:
        return False, None
