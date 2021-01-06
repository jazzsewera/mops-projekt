class SimulationParameters(object):
    def __init__(
        self,
        simulation_time: float,
        packet_length: int,
        generation_constant: float,
        queue_constant: float,
        streams_number: int,
        dropped_streams: int,
    ):
        self.simulation_time = simulation_time
        self.packet_length = packet_length
        self.generation_constant = generation_constant
        self.queue_constant = queue_constant
        self.streams_number = streams_number
        self.dropped_streams = dropped_streams
