import logging as log

from simulator.timer import Timer


class PacketGenerator(object):
    def __init__(self, timer, packet_length, generation_time):
        log.debug("New packet stream created")
        self._current_time = 0
        self._on_time_start = 0
        self._on_time = 0
        self._off_time_start = 0
        self._off_time = 0

        self._timer: Timer = timer
        self._packet_length = packet_length
        self._generation_time = generation_time
        self._time_counter = 0
        self._is_state_on = True
        self._is_passing = True  # flag describing whether we pass a packet to next server or drop it after leaving previous

    def generator_event_listener(self, current_time):
        self._current_time = current_time
        if self._current_time < self._on_time_start + self._on_time:
            log.debug("Sending packet from generator")
            pass  # send event
            self._timer.confirm_clock()
        elif self._current_time < self._off_time_start + self._off_time:
            self._timer.confirm_clock()
        else:
            # generate next on_time and off_time
            self._on_time = 5  # get random
            self._off_time = 3  # get random
            self._on_time_start = self._current_time
            self._off_time_start = self._current_time + self._on_time
            self.generator_event_listener(self._current_time)
