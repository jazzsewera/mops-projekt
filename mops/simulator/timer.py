import logging as log
from .event import Event
from threading import Thread
from numpy import random
import time


class Timer(object):
    def __init__(self, simulation_time, p_on, p_off):
        self._simulation_time = simulation_time
        self._p_on = p_on
        self._p_off = p_off

        self._on_event = Event()
        self._off_event = Event()
        self._simulation_stop_event = Event()
        self._is_simulation_running = True

        log.debug(f"Event object {self._on_event}")
        log.debug(f"Self: {self}")

        self._simulation_stop_event.add_handler(self._set_stop_simulation_flag)

    def register_on_event_handler(self, handler):
        log.debug(f"Event in register on event: {self._on_event}")
        self._on_event.add_handler(handler)
        log.debug(f"Event in register on event: {self._on_event}")

    def register_off_event_handler(self, handler):
        self._off_event.add_handler(handler)

    def print_on_event(self):
        log.debug(f"On event: {self._on_event}")

    def launch_timer_threads(self):
        log.debug(f"Self: {self}")
        log.debug(f"On event object: {self._on_event}")
        log.debug(f"Off event object: {self._off_event}")
        simulation_timer = Thread(target=self._start_simulation_timer, args=[])
        timer_event_loop = Thread(target=self._start_timer_event_loop, args=(self._on_event, self._off_event))
        simulation_timer.start()
        timer_event_loop.start()
        simulation_timer.join()
        timer_event_loop.join()

    def _set_stop_simulation_flag(self):
        self._is_simulation_running = False

    def _start_timer_event_loop(self, on_event, off_event):
        while self._is_simulation_running:
            time.sleep(random.exponential(self._p_on))
            log.debug("Firing on event")
            log.debug(f"Event object {on_event}")
            on_event()
            time.sleep(self._p_off)
            log.debug("Firing off event")
            log.debug(f"Event object {off_event}")
            off_event()

    def _start_simulation_timer(self):
        time.sleep(self._simulation_time)
        self._set_stop_simulation_flag()
        log.debug("Simulation timer ended")
