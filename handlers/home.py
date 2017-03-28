# coding: utf-8

import markdown
from tornado.web import HTTPError
from tornado.web import authenticated

import model
from .base import BaseHandler
from utils.session import DBSession


class Home(BaseHandler):
    def get(self):
        #TODO: pane module
        node = self.get_secure_cookie("node", "home")

        
        panes = self.session.query(model.Pane).filter_by(module="home").all()
        return self.render('home.html', panes=panes)


urls = [
    (r"/", Home),
]
