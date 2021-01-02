from numpy import random


class Rand(object):
    def __init__(self, lambda_on, lambda_off):
        self._lambda_on = lambda_on
        self._lambda_off = lambda_off

    def generate_random_on_time(self):
        # TODO: check implementation
        return random.exponential(1 / self._lambda_on)

    def generate_random_off_time(self):
        # TODO: check implementation
        return random.exponential(1 / self._lambda_off)
