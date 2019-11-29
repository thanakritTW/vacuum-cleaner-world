class BasedSensor:

    def __init__(self, cleaner, environment):
        self._cleaner = cleaner
        self._environment = environment

    def _get_coordinate_point(self, cleaner):
        grids = self._environment.grids()
        x, y = cleaner.position()
        max_index = len(grids) - 1
        return max_index - y, x

    def set_cleaner(self, cleaner):
        self._cleaner = cleaner