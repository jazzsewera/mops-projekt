import logging as log

class PacketGenerator(object):
    def __init__(self, packet_length, generation_time):
        log.debug("New packet stream created")

        self._packet_length = packet_length
        self._generation_time = generation_time
        self._packets_buffer_arrival_times = [] # times of packets arrival in buffer
        self._time_counter = 0
        self._is_state_on = True
        self._is_passing = True # flag describing wheteher we pass packet to next server or drop it after leaving previous

    def generate_packets(self, on_time, off_time):
        while True:
            if _is_state_on:
                on_time += self._time_counter
                while self._time_counter <= on_time:
                    self._packets_buffor_arrival_times.append(self._time_counter + _generation_time)
                    self._time_counter += _generation_time
                _time_counter = on_time
                is_state_on = False

            if not _is_state_on:
                _time_counter += off_time
                is_state_on = True