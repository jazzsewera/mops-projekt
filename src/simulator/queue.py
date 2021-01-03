import logging as log

from simulator.timer import Timer
from simulator.packet import Packet


class Queue(object):
    def __init__(self, timer):
        log.debug("New queue created")
        self.packets = []
        self._timer: Timer = timer

    def queue_packet_receiver(self, in_queue_time):
        packet = Packet(in_queue_time)
        self.packets.append(packet)
