import logging as log


class Timer(object):
    def __init__(self, simulation_time):
        self._simulation_time = simulation_time
        self._current_time = 0.0

    @property
    def current_time(self) -> float:
        if self._current_time < self._simulation_time:
            return self._current_time
        else:
            exit()  # send event to report creator

    @current_time.setter
    def current_time(self, new_time: float) -> None:
        if self._current_time > new_time:
            log.warning("New time is earlier than current!")
        self._current_time = new_time
