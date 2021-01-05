import logging as log

from simulator.event_queue import Event, EventQueue
from simulator.packet import Packet
from simulator.queue import Queue
from simulator.rand import Rand
from simulator.timer import Timer


class PacketGenerator(object):
    def __init__(
        self,
        timer: Timer,
        event_queue: EventQueue,
        queue: Queue,
        packet_length: int,
        generation_time: float,
        is_passing: bool,
    ):
        log.debug("New packet stream created")
        self._on_time_start = 0
        self._on_time = 0
        self._off_time_start = 0
        self._off_time = 0

        self._timer = timer
        self._event_queue = event_queue
        self._queue = queue
        self._rand = Rand(0.5, 0.3)  # set lambda1 and lambda2 on start
        self._packet_length = packet_length
        self._generation_time = generation_time
        self._time_counter = 0
        self._is_passing = is_passing  # flag describing whether we pass a packets to next server or drop it after leaving previous
        self._is_state_on = True

    def _send_packet(self, event: Event):
        packet = Packet(event.when, self._is_passing)
        self._queue.queue_packet_receiver(packet)

    def _end_packet_generation(self, event: Event):
        event = Event(
            True,
            event.when + self._generation_time,
            "End packet generation",
            self._send_packet,
        )
        self._event_queue.add_event(event)

    def generate_packet(self):
        event = Event(
            False,
            self._timer.current_time,
            "Start packet generation",
            self._end_packet_generation,
        )
        self._event_queue.add_event(event)

        # generate next on_time and off_time
        #  self._on_time = self._rand.generate_random_on_time()
        #  self._off_time = self._rand.generate_random_off_time()
        #  self._on_time_start = self._timer.current_time
        #  self._off_time_start = self._timer.current_time + self._on_time
