import logging as log


class HandledEvent(object):
    def __init__(self):
        log.debug("[Event] __init__")
        self.handlers = []

    def add_handler(self, handler):
        log.debug(f"[Event] added {handler}")
        self.handlers.append(handler)

    def remove_handler(self, handler):
        self.handlers.remove(handler)

    def __call__(self, *args, **kwargs):
        log.debug("[Event] __call__")
        for handler in self.handlers:
            handler(*args, **kwargs)
