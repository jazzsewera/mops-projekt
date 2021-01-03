import logging as log
from threading import Thread
import time

from .event import Event
from .rand import Rand


class Timer(object):
    def __init__(self, rand, simulation_time):
        self._rand: Rand = rand
        self._simulation_time = simulation_time

        self._on_event = Event()
        self._off_event = Event()
        self._simulation_stop_event = Event()
        self._is_simulation_running = True

        self._simulation_stop_event.add_handler(self._set_stop_simulation_flag)

    def register_on_event_handler(self, handler):
        self._on_event.add_handler(handler)

    def register_off_event_handler(self, handler):
        self._off_event.add_handler(handler)

    def launch_timer_threads(self):
        simulation_timer = Thread(target=self._start_simulation_timer, args=[])
        timer_event_loop = Thread(
            target=self._start_timer_event_loop, args=(self._on_event, self._off_event)
        )
        simulation_timer.start()
        timer_event_loop.start()
        simulation_timer.join()
        timer_event_loop.join()

    def _set_stop_simulation_flag(self):
        self._is_simulation_running = False

    def _start_timer_event_loop(self):
        while self._is_simulation_running:
            time.sleep(self._rand.generate_random_on_time())
            self._on_event()
            time.sleep(self._rand.generate_random_off_time())
            self._off_event()

    def _start_simulation_timer(self):
        time.sleep(self._simulation_time)
        self._set_stop_simulation_flag()
        log.debug("Simulation timer ended")
