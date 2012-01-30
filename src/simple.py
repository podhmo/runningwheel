from fanstatic import Fanstatic
from js.jquery import jquery

def app(environ, start_response):
    import pdb; pdb.set_trace()
    jquery.need()
    start_response('200 OK', [])
    return ['<html><head></head><body></body></html>']

fanstatic_app = Fanstatic(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8080, fanstatic_app)
    server.serve_forever()
