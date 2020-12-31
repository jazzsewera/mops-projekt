class Report(object):
    def __init__(self):
        self._packets_in_buffer = []
        self._packet_wait_time = []
        self._server_load = []

    def update_state(self, packets_in_buffer, packet_wait_time, server_load):
        self._packets_in_buffer.append(packets_in_buffer)
        self._packet_wait_time.append(packet_wait_time)
        self._server_load.append(server_load)
