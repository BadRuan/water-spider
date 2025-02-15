# 被观察者：爬虫基类
class SpierSubject:
    def __init__(self):
        self._handlers = set()

    def register_handler(self, handler):
        self._handlers.add(handler)

    def unregister_handler(self, handler):
        self._handlers.discard(handler)

    def notify_handler(self, data):
        for handler in self._handlers:
            handler.on_data_received(data)
