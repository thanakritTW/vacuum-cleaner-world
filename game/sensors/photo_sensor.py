from game.sensors.sensor import BasedSensor


class PhotoSensor(BasedSensor):
    def __init__(self, cleaner, environment):
        super().__init__(cleaner, environment)

    def run(self):
        i, j = self._get_coordinate_point(self._cleaner)
        grids = self._environment.grids()
        return grids[i][j]
