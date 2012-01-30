from webdispatch import URLDispatcher
from webob import Request
from webob.dec import wsgify
from webdispatch.mixins import URLMapperMixin
from staticserve import StaticServeView
from service import Service
import os

class MyRequest(Request, URLMapperMixin):
    pass

class WebObDispatcher(URLDispatcher):
    def add_url(self, name, pattern, view):
        application = wsgify(view, RequestClass=MyRequest)
        super(WebObDispatcher, self).add_url(name, pattern, application)


def hello_view(request):
    return get_service().get_template("hello.mak").render()

_service = Service({"template.path": os.path.join(".", "templates")})

def get_service():
    global _service
    return _service

def make_app():
    global _service
    app = WebObDispatcher()
    app.add_url("hello", "/", hello_view)
    app.add_url("statics", "/statics/*", StaticServeView(".").view)
    return app

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    import sys
    sys.stderr.write("port 6543")
    app = make_app()
    httpd = make_server('0.0.0.0', 6543, app)
    httpd.serve_forever()
