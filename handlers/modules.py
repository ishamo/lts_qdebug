# coding: utf-8

import tornado.web 
from tornado.web import HTTPError

class PaneModule(tornado.web.UIModule):
    def render(self, pane):
        return self.render_string("modules/pane.html", pane)


class GatherModule(tornado.web.UIModule):
    def render(self, post_id):
        with DBSession() as sess:
            post_ = sess.query(Post_).filter_by(post_id=post_id).first()
            if not post_:
                raise HTTPError(400, error="post_id")
            user = sess.query(User).filter_by(id_=post_.user_id).first()
            if not user:
                raise HTTPError(400, error="user_id")
            answers = sess.query(Answer).filter_by(post_id=post_.id_).all()
        return self.render_string("modules/gather.html", post_, user, answers)



