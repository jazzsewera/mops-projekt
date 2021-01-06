import math

from logger import Logger
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
        generation_constant: float,
        is_passing: bool,
    ):
        self.log = Logger(self)
        self.log.debug("New packet stream created")
        self._on_time_start = 0
        self._on_time = 0
        self._off_time_start = 0
        self._off_time = 0

        self._timer = timer
        self._event_queue = event_queue
        self._queue = queue
        self._rand = Rand(0.2, 0.2)  # set lambda1 and lambda2 on start
        self._packet_length = packet_length
        self._generation_time = packet_length * generation_constant
        self._time_counter = 0
        self._is_passing = is_passing  # flag describing whether we pass a packets to next server or drop it after leaving previous
        self._is_state_on = False

        self._switch_state(
            Event(
                None,
                0,
                "Switch queue state (1st)",
                self._switch_state,
            )
        )

    def _send_packet(self, event: Event):
        packet = Packet(event.when, self._is_passing)
        self._queue.queue_packet_receiver(packet)

    def _end_packet_generation(self, event: Event):
        event = Event(
            True,
            event.when + self._generation_time,
            event.summary,
            self._send_packet,
        )
        self.log.warn("Sending packet to queue from generator")
        self._event_queue.add_event(event)

    def generate_packets(self, time):
        for i in range(math.floor(self._on_time / self._generation_time)):
            self.log.debug(
                f"Adding packet generation for {time + i * self._generation_time}"
            )
            self.log.debug(
                f"event.when={time}, i={i}, self._generation_time={self._generation_time}"
            )
            _event = Event(
                False,
                time + i * self._generation_time,
                "Packet generation",
                self._end_packet_generation,
            )
            self._event_queue.add_event(_event)

    def generate_packets_events(self, time):
        for i in range(math.floor(self._on_time / self._generation_time)):
            _event = Event(
                False,
                time + i * self._generation_time,
                "Packet generation",
                self._end_packet_generation,
            )
            self._event_queue.add_event(_event)

    def _switch_state(self, event: Event):
        if self._is_state_on:
            r_time = self._rand.generate_random_off_time()
            event_summary = f"Switch generator state to ON after {r_time:.2f}"
        else:
            r_time = self._rand.generate_random_on_time()
            event_summary = f"Switch generator state to OFF after {r_time:.2f}"
            self._on_time = r_time
            self.generate_packets(event.when)

        event = Event(
            None,
            event.when + r_time,
            event_summary,
            self._switch_state,
        )
        self._event_queue.add_event(event)

        self._is_state_on = not self._is_state_on
