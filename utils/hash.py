from hashlib import sha1

from setup import salt


def hash_password(unhashed_password):
    # I do not expect password to be given in bytes, but if for any ill reason this happens in future I want
    # to be error-prone.
    if isinstance(unhashed_password, str):
        return sha1(unhashed_password.encode('utf-8') + salt).hexdigest()
    else:
        raise TypeError('unhashed_password must be utf-8 string')
