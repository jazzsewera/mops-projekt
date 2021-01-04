import logging as log

from simulator.packet import Packet
from simulator.queue import Queue
from simulator.rand import Rand
from simulator.timer import Timer


class PacketGenerator(object):
    def __init__(self, timer, queue, packet_length, generation_time):
        log.debug("New packet stream created")
        self._current_time = 0
        self._on_time_start = 0
        self._on_time = 0
        self._off_time_start = 0
        self._off_time = 0

        self._timer: Timer = timer
        self._queue: Queue = queue
        self._rand = Rand(0.5, 0.3)  # set lambda1 and lambda2 on start
        self._packet_length = packet_length
        self._generation_time = generation_time
        self._time_counter = 0
        self._is_state_on = True
        self._is_passing = True  # flag describing whether we pass a packet to next server or drop it after leaving previous

    def generator_event_listener(self, current_time):
        self._current_time = current_time
        if self._current_time < self._on_time_start + self._on_time:
            packet = Packet(self._current_time + self._generation_time)
            log.debug(f"Sending packet: {packet} from generator")
            self._queue.queue_packet_receiver(packet)
            self._timer.confirm_clock()
        # jeszcze jeden if if self current time == self.ontimestart + iterator (leci od zera) i zwieksza sie o 1 co wysłany pakiet * generation time
        elif self._current_time < self._off_time_start + self._off_time:
            self._timer.confirm_clock()
        else:
            # generate next on_time and off_time
            self._on_time = self._rand.generate_random_on_time()
            self._off_time = self._rand.generate_random_off_time()
            self._on_time_start = self._current_time
            self._off_time_start = self._current_time + self._on_time
            self.generator_event_listener(self._current_time)
