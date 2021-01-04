import logging as log
from typing import Optional

from simulator.packet import Packet
from simulator.timer import Timer


class Queue(object):
    def __init__(self, timer, packet_length, queue=None):
        log.debug("New queue created")
        self.packets = []
        self._timer: Timer = timer
        self._queue: Optional[Queue] = queue
        self._current_time = 0
        self._service_time = 2 * packet_length
        self._service_time_start = 0
        self._last_packets_number = 0
        self.packets_number = {}
        self._current_packet = None
        self._current_packet_remaining_time = 0

    def queue_packet_receiver(self, packet: Packet):
        self.packets.append(packet)

    def queue_packet_listener(self, current_time):
        self.packets_number[current_time] = len(self.packets)

        self._current_time = current_time
        if self.packets and not self._current_packet:
            self._current_packet = self.packets.pop(0)
            self._current_packet_remaining_time = self._service_time - 1
            self._service_time_start = self._current_time
            self._current_packet.out_of_queue_time = self._service_time_start
        elif self._current_packet and self._current_packet_remaining_time:
            self._current_packet_remaining_time -= 1
            log.debug(f"Server busy, currently handling packet: {self._current_packet}")
        elif self._current_packet and not self._current_packet_remaining_time:
            self._current_packet.in_second_queue_time = self._current_time
            log.info(f"Finished handling packet: {self._current_packet}")
            if self._queue:
                # TODO: decide if the packet should be sent
                self._queue.queue_packet_receiver(self._current_packet)
            self._current_packet = None
        else:
            log.info("Queue is empty")

        self._timer.confirm_clock()
