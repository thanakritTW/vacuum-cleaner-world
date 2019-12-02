from game.sensors.sensor import BasedSensor
from game.service import UtilService


class PhotoSensor(BasedSensor):
    def __init__(self, cleaner, environment):
        super().__init__(cleaner, environment)

    def run(self):
        i, j = UtilService.get_coordinate_point(self._cleaner, self._environment)
        grids = self._environment.grids()
        return grids[i][j]
