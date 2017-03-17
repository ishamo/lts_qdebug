# coding: utf-8

from tornado.web import HTTPError

from model import *
from utils.session import DBSession


def get_post_by_nodeid(node_id, limit, offset):
    with DBSession() as sess:
        node = sess.query(Node).filter_by(id_=node_id).first()
        if not node:
            raise HTTPError(404, "node_id")

        posts_ = sess.query(desc(Post_.updated_at)).filter_by(node_id =node_id).\
                limit(limit).offset(offset).all()

        return posts_



