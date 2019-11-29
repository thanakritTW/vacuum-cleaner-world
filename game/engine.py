from game.cleaner import Cleaner
from game.environment import Environment


class Engine:
    def __init__(self, cleaner: Cleaner, environment: Environment):
        self._latest_cleaner = cleaner
        self._history = [cleaner]
        self._environment = environment
        self._home_position = cleaner.position()

    def sensors(self):
        return self.touch_sensor(), self.photosensor(), self.infrared_sensor()

    def touch_sensor(self):
        cleaner = self._latest_cleaner.act("go_forward")
        i, j = self._get_coordinate_point(cleaner)
        return self._is_bumbed(i, j) * 1

    def photosensor(self):
        i, j = self._get_coordinate_point(self._latest_cleaner)
        grids = self._environment.grids()
        return grids[i][j]

    def infrared_sensor(self):
        return self._home_position == self._latest_cleaner.position()

    def _get_coordinate_point(self, cleaner):
        grids = self._environment.grids()
        x, y = cleaner.position()
        max_index = len(grids) - 1
        return max_index - y, x

    def _is_bumbed(self, i, j):
        grids = self._environment.grids()
        _is_bumbed_y = i > len(grids) or i < 0
        _is_bumbed_x = j > len(grids[i]) or j < 0
        return _is_bumbed_x or _is_bumbed_y