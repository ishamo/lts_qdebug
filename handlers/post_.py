# coding: utf-8

import markdown
from tornado.web import HTTPError
from tornado.web import authenticated

import model
from .base import BaseHandler
from utils.session import DBSession

class PostHandler(BaseHandler):
    def get(self, post_id):
        with DBSession() as sess:
            post_ = sess.query(Post_).filter_by(id_=post_id).first()
            if not post_:
                raise HTTPErorr(404)
            return self.render('post_.html', post_)

    @authenticated
    def post(self):
        title = self.get_argument('title', '')
        markdown = self.get_argument('text', '')
        node_id = self.get_argument('node', '')
        topic_ids = self.get_argment('topics' '')

        if title == '' or markdown == '' or node == '' or topics == []:
            self.redirect(self.get_query_argument('next_', '/'))

        with DBsession as sess:
            post_ = model.Post_(title=title, markdown=markdown,
                    html=markdown.markdown(markdown), user_id=self.current_user.id_,
                    node_id=node_id)
            sess.add(post_) 
            post_topics = [model.Post_Topic(post_id=post_.id_, topic_id=topic_id) \
                    for topic_id in topic_ids]
            sess.add_all(post_topics)
            sess.commit()

        return self.redirect('/posts/%s' % post_.id_)

    @authenticated
    def put(self):
        pass

    @authenticated
    def delete(self):
        pass


urls = []





