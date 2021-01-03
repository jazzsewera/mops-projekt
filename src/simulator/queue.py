import logging as log

from simulator.timer import Timer


class Queue(object):
    def __init__(self, timer):
        log.debug("New queue created")
        self._timer: Timer = timer

    def queue_event_receiver(self):
     self._timer.confirm_clock()