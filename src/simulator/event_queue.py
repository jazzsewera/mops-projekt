from typing import Callable, List, Optional

from logger import Logger
from simulator.timer import Timer


class Event(object):
    def __init__(
        self,
        is_event_end: Optional[bool],
        when: float,
        summary: str,
        on_handle: Optional[Callable] = None,
    ):
        self.is_event_end = is_event_end
        self.when = when
        self.summary = summary
        self.on_handle = on_handle

    def __repr__(self):
        if self.is_event_end is not None:
            event_type = "END" if self.is_event_end else "START"
        else:
            event_type = "SINGLE"
        return f"[Event@{self.when:.2f}] {event_type} {self.summary}"


class EventQueue(object):
    def __init__(self, simulation_time: float, timer: Timer):
        self.log = Logger(self)
        self._simulation_time = simulation_time
        self._timer = timer
        self.queue: List[Event] = []

    def add_event(self, event: Event):
        self.log.debug(f"ADD | {event}")
        self.queue.append(event)
        self.queue.sort(key=lambda e: e.when)
        self.log.debug(f"event list length: {len(self.queue)}")

    def handle_event(self) -> bool:
        if self._timer.current_time > self._simulation_time:
            self.log.debug("Simulation time ended")
            return False
        if self.queue:
            event = self.queue.pop(0)
            self.log.info(f"HANDLE | {event}")
            self._timer.current_time = event.when
            if event.on_handle:
                event.on_handle(event)
            else:
                self.log.debug(f"NOT HANDLED | {event}")
            return True
        else:
            self.log.debug("Event queue empty")
            return False
