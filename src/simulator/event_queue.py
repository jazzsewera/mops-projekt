import logging as log
from typing import Callable, List, Optional

from simulator.timer import Timer


class Event(object):
    def __init__(
        self,
        is_event_end: bool,
        when: float,
        summary: str,
        on_handle: Optional[Callable] = None,
    ):
        self.is_event_end = is_event_end
        self.when = when
        self.summary = summary
        self.on_handle = on_handle

    def __repr__(self):
        return f"[Event@{self.when}] {'END' if self.is_event_end else 'START'} {self.summary}"


class EventQueue(object):
    def __init__(self, timer: Timer):
        self._timer = timer
        self.queue: List[Event] = []

    def add_event(self, event: Event):
        log.debug(f"{event} | added")
        self.queue.append(event)
        self.queue.sort(key=lambda e: e.when)

    def handle_event(self) -> bool:
        if self.queue:
            event = self.queue.pop(0)
            if event.is_event_end:
                self._timer.current_time = event.when
            if event.on_handle:
                event.on_handle(event)
            else:
                log.debug(f"{event} | did not have on_handle()")
            return True
        else:
            log.debug("Event queue empty")
            return False
