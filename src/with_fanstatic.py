import fanstatic
from js.jquery import jquery

class WithFanstaticFactory(object):
    def __init__(self, **config):
        self.config = config
    
    def need_fanstatic(self):
        jquery.need()

    def create(self):
        def with_fanstatic(view):
            def decorated(request):
                # injector
                needed = fanstatic.init_needed(**self.config)
                request.environ[fanstatic.NEEDED] = needed

                self.need_fanstatic()
                response =  view(request)
                if not (response.content_type and
                        response.content_type.lower() in ['text/html',
                                                          'text/xml']):
                    fanstatic.del_needed()
                    return response

                if needed.has_resources():
                    result = needed.render_topbottom_into_html(response.body)
                    response.body = ''
                    response.write(result)
                fanstatic.del_needed()
                return response
            return decorated
        return with_fanstatic

with_fanstatic = WithFanstaticFactory().create()
