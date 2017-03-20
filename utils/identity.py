# coding: utf-8


import functools

import model
from utils.session import DBSession


def admin_required(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        headers = self.request.headers
        user_id = headers['user_id']
        token_string = headers['token_string']

        with DBSession() as sess:
            user = sess.query(User).filter_by(id_=user_id).first()
            if not user or not user.role == 'admin':
                raise HTTPError(403, "admin needed")
            token = sess.query(Token).filter_by(user_id=user_id).first()
            if not token or not token.token_string == token_string:
                raise HTTPError(403, "login needed")

        return func(self, *args, **kwargs)
    return wrapper

