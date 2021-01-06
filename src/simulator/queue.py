from typing import Optional

from logger import Logger
from simulator.event_queue import Event, EventQueue
from simulator.packet import Packet
from simulator.timer import Timer


class Queue(object):
    def __init__(
        self, timer: Timer, event_queue: EventQueue, packet_length: int, queue=None
    ):
        self.log = Logger(self)
        self.log.debug("New queue created")
        self.packets = []
        self.packets_passed = []
        self._timer = timer
        self._event_queue = event_queue
        self._queue: Optional[Queue] = queue
        self._current_time = 0.0
        self._service_time = 2.0 * packet_length
        self._service_time_start = 0.0
        self._last_packets_number = 0
        self._metrics_delta = 1.0
        self.packets_number = {}
        self._current_packet: Optional[Packet] = None
        self._current_packet_remaining_time = 0.0

        #self._get_metrics(Event(None, 0.0, "Get queue metrics", self._get_metrics))

    def _end_packet_handling(self, event: Event):
        event = Event(
            True, event.when + self._service_time, event.summary, self._send_packet
        )
        self._event_queue.add_event(event)

    def _send_packet(self, event: Event):
        if self._current_packet is not None:
            if self._queue is None:
                self._current_packet.out_of_second_queue = event.when - self._service_time
                self._current_packet.out_of_system_time = event.when
                self.packets_passed.append(self._current_packet)
            else:
                self._current_packet.out_of_queue_time = event.when - self._service_time
                self._current_packet.in_second_queue_time = event.when
                self._queue.queue_packet_receiver(self._current_packet)

                if self._current_packet.is_passing:
                    self._queue.queue_packet_receiver(self._current_packet)
                    self.packets_passed.append(self._current_packet)
        else:
            self.log.error(
                "self._current_packet is None "
                "when self._send_packet() method was called!"
            )

        self._start_packet_handling(event.when)

    def _start_packet_handling(self, start_time: float):
        if not self.packets:
            self.log.info("Queue is empty")
            self._current_packet = None
            return

        self._current_packet = self.packets.pop(0)
        self.packets_number[self._timer.current_time] = len(self.packets)
        event = Event(False,
                      start_time + self._service_time,
                      "Packet handling",
                      self._send_packet)
        self._event_queue.add_event(event)

    def queue_packet_receiver(self, packet: Packet):
        if self._queue is None and packet.out_of_queue_time == 0:
            packet.in_second_queue_time = packet.in_queue_time
            packet.in_queue_time = 0.0

        self.packets.append(packet)
        self.packets_number[self._timer.current_time] = len(self.packets)
        #self.log.info(f"RECEIVE | {packet}")
        #self.log.debug(f"Number of packets: {len(self.packets)}")

        if self._current_packet is None:
            if self._queue is not None:
                self._start_packet_handling(packet.in_queue_time)
            else:
                self._start_packet_handling(packet.in_second_queue_time)

    def _get_metrics(self, event: Event):
        self.packets_number[self._timer.current_time] = len(self.packets)
        event = Event(
            None, event.when + self._metrics_delta, event.summary, self._get_metrics
        )
        self._event_queue.add_event(event)
