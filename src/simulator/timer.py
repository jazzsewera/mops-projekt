import logging as log
from threading import Thread
from time import sleep

from .event import Event


class Timer(object):
    def __init__(self, simulation_time):
        self._simulation_time = simulation_time
        self.current_time = 0

        self._clock_event = Event()
        self._connected_listeners = 0

        self._confirmed_listeners = 0
        self._confirmed_listeners_mutex = False

    def add_clock_event_listener(self, listener):
        """
        Listeners should be methods that take one argument, e.g.
        `listener(current_time: int)`
        """
        self._clock_event.add_handler(listener)
        self._connected_listeners += 1

    def remove_clock_event_listener(self, listener):
        self._clock_event.remove_handler(listener)
        self._connected_listeners -= 1

    def confirm_clock(self):
        while self._confirmed_listeners_mutex:
            sleep(0.01)
        self._confirmed_listeners_mutex = True
        self._confirmed_listeners += 1
        log.debug(f"Confirmed listeners: {self._confirmed_listeners}")
        self._confirmed_listeners_mutex = False

    def launch_timer_thread(self):
        self._timer_event_loop = Thread(target=self._start_timer_event_loop, args=[])
        self._timer_event_loop.start()

    def join_timer_thread(self):
        self._timer_event_loop.join()

    def _start_timer_event_loop(self):
        while self.current_time < self._simulation_time:
            # TICK
            self._clock_event(self.current_time)
            log.debug(f"Current clock: {self.current_time}")
            # TOCK
            while self._confirmed_listeners < self._connected_listeners:
                sleep(0.01)  # sleep a little bit not to overwhelm processor
                log.debug(
                    f"Current time: {self.current_time}. "
                    "Some listeners did not confirm that they finished"
                )
            self._confirmed_listeners = 0
            self.current_time += 1
