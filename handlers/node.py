# coding: utf-8

import markdown
from tornado.web import HTTPError
from tornado.web import authenticated

from model import *
from .base import BaseHandler
from utils.session import DBSession
from utils.identity import admin_required
from api.nodeLite import get_post_by_nodeid


class Node(BaseHandler):
    def get(self):
        """实际上是创建node的那个页面，这么写是错的！！！"""
        return self.render('node.html', error=None)

    @admin_required
    def post(self):
        label = self.get_body_argument("label", "")
        if label == "":
            return self.render('node.html', error="label")
        with DBSession() as sess:
            node = sess.query(Node).filter_by(label=label).first()
            if node:
                return self.render(node.html, error="label exist")
            node = Node(label=label)
            sess.add(node); sess.commit()
        return self.redirect("/") # !

    @admin_required
    def put(self, node_id):
        label = self.get_body_argument("label", "")
        if label == "":
            return self.render("node.html", error="label")
        with DBSeesion() as sess:
            pass # todo

    @admin_required
    def delete(self, node_id):
        pass
        pass


