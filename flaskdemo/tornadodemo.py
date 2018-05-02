import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class DomainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, a.com")


application = tornado.web.Application([
    (r"/.com", MainHandler),
])
# application.add_handlers(r"^a\.com$", [
#     (r"/", DomainHandler),
# ])
application.add_handlers(r"^a.com.ss\$", [
    (r"/", DomainHandler),
])
application.add_handlers(r"^(www/.)?a/.com$", [(r"/", DomainHandler),])
if __name__ == "__main__":
    debug = True
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()