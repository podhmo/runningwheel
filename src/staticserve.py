from webob import Response
import webob.exc as exc
import mimetypes
import os
    
class StaticServeView(object):
    def __init__(self, root_path, block_size=4096*64):
        self.root_path = root_path
        self.block_size = block_size

    def get_file_path(self, path):
        path = os.path.join(self.root_path, path)
        if os.path.exists(path):
            return path
        else:
            raise exc.HTTPNotFound("file not found")
        
    def serve(self, request):
        response = Response()
        path = self.get_file_path(request.path[1:])
        self.settings(response, path)
        return response

    def settings(self, response, path):
        content_type, content_encoding = mimetypes.guess_type(path, strict=False)
        if content_type is None:
            content_type = "application/octet-stream"

        response.content_type = content_type
        response.content_encoding = content_encoding
        response.content_length = os.path.getsize(path)
        f = open(path, "rb")
        response.app_iter = _FileIter(f, self.block_size)


    def view(self, request):
        return self.serve(request)
        
class _FileIter(object):
    def __init__(self, file, block_size):
        self.file = file
        self.block_size = block_size

    def __iter__(self):
        return self

    def next(self):
        val = self.file.read(self.block_size)
        if not val:
            raise StopIteration
        return val

    __next__ = next # py3

    def close(self):
        self.file.close()
