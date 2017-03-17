# coding: utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        headers = self.request.headers
        if "username" in self.headers:
            username = self.headers.get("username")
        else:
            username = self.get_secure_cookie("username")
        if username == "":
            return None
        user = self.session.query(User).filter_by(username==username).first()
        if not user:
            return None

        token_string = headers.get("token", "")
        if token_string == "": return None
        token = self.session.query(Token).filter_by(token_string==token_sstring).first()
        if not token:
            return None
        if not token.uid == user.uid:
            return None
        return user


    @propety
    def session(self):
        return session

    def on_finish(self):
        self.session.remove()