class State(object):
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
