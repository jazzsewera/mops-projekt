import logging as log


class Timer(object):
    def __init__(self):
        self._current_time = 0.0

    @property
    def current_time(self) -> float:
        return self._current_time

    @current_time.setter
    def current_time(self, new_time: float) -> None:
        if self._current_time > new_time:
            log.warning("New time is earlier than current!")
        self._current_time = new_time
