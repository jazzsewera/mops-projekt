import logging as log

from simulator.packet import Packet
from simulator.timer import Timer


class Queue(object):
    def __init__(self, timer):
        log.debug("New queue created")
        self.packets = []
        self._timer: Timer = timer

    def queue_packet_receiver(self, in_queue_time):
        packet = Packet(in_queue_time)
        self.packets.append(packet)
