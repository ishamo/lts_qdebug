# coding: utf-8

import os

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from handlers.urls import urls
import settings


class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="asldfasjdfas",
            login_url="/login",
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)


def main():
    app = Application()
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(settings.SERVER_PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
