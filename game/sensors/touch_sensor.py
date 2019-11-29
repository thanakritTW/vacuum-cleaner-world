from game.sensors.sensor import BasedSensor


class TouchSensor(BasedSensor):
    def __init__(self, cleaner, environment):
        super().__init__(cleaner, environment)

    def run(self):
        trying_cleaner = self._cleaner.act("go_forward")
        i, j = self._get_coordinate_point(trying_cleaner)
        return self._is_bumped(i, j) * 1

    def _is_bumped(self, i, j):
        square_grids = self._environment.grids()
        length = len(square_grids)
        is_out_off_vertical_bound = i >= length or i < 0
        is_out_off_horizontal_bound = j >= length or j < 0
        return is_out_off_vertical_bound or is_out_off_horizontal_bound
