class RedisService(object):
    def __init__(self, url=None, port=None):#todo fix
        self.url = url or "127.0.0.1"
        self.port = port or 6379
        self.redis = redis.Redis(url, port)

    def save(self, k, v):
        self.redis.set(k, v)

    def load(self, k):
        self.load(k)

