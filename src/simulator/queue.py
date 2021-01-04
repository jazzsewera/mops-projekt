import logging as log
from collections import deque

from simulator.packet import Packet
from simulator.timer import Timer


class Queue(object):
    def __init__(self, timer, packet_length):
        log.debug("New queue created")
        self.packets = deque()
        self._timer: Timer = timer
        self._current_time = 0
        self._service_time = 2 * packet_length
        self._service_time_start = 0
        self._packets_number = {}

    def queue_packet_receiver(self, packet: Packet):
        self.packets.append(packet)

    def queue_packet_listener(self, current_time):
        self._current_time = current_time
        self._packets_number[current_time] = len(self.packets)
        if len(self.packets) != 0:
            log.debug("Queue not empty")
            if self._current_time >= self._service_time_start + self._service_time:
                #sending done packet
                packet = self.packets.popleft()
                packet.out_of_queue_time = self._service_time_start
                packet.in_second_queue_time = current_time
                log.debug(f"Sending packet: {packet} from queue to server")
                #self._queue.queue_packet_receiver(packet)
                #starting service of new packet
                self._service_time_start = current_time#to do
                self._timer.confirm_clock()

            elif self._current_time < self._service_time_start + self._service_time:
                self._timer.confirm_clock()
                log.debug("Server busy")
        else:
            self._service_time_start = current_time
            self._timer.confirm_clock()
            log.debug("Queue is empty")