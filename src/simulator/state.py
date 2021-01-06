class SimulationTime(object):
    _simulation_time = 0

    def __init__(self):
        raise RuntimeError("Call get() instead")

    @classmethod
    def get(cls):
        return cls._simulation_time

    @classmethod
    def set(cls, time):
        cls._simulation_time = time

    @classmethod
    def increment(cls):
        cls._simulation_time += 1


class GeneratorParameters(object):
    _packet_length = 0
    _generation_time = 0.0
    _streams_number = 0
    _dropped_streams = 0

    def __init__(self):
        raise RuntimeError("Call get() instead")

    @classmethod
    def get_packet_length(cls):
        return cls._packet_length

    @classmethod
    def set_packet_length(cls, packet_length):
        cls._packet_length = int(packet_length)

    @classmethod
    def get_generation_time(cls):
        return cls._generation_time

    @classmethod
    def set_generation_time(cls, generation_time):
        cls._generation_time = float(generation_time)

    @classmethod
    def get_streams_number(cls):
        return cls._streams_number

    @classmethod
    def set_streams_number(cls, streams_number):
        cls._streams_number = int(streams_number)

    @classmethod
    def get_dropped_streams(cls):
        return cls._dropped_streams

    @classmethod
    def set_dropped_streams(cls, dropped_streams):
        cls._dropped_streams = int(dropped_streams)
