from game.cleaner import Cleaner
from game.environment import Environment


class Engine:
    def __init__(self, cleaner: Cleaner, environment: Environment):
        self._latest_cleaner = cleaner
        self._history = [cleaner]
        self._environment = environment

    def sensors(self):
        NotImplementedError

    def touch_sensor(self):
        NotImplementedError

    def _get_coordinate_point(self):
        NotImplementedError