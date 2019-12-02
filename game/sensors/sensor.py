class BasedSensor:

    def __init__(self, cleaner, environment):
        self._cleaner = cleaner
        self._environment = environment

    def set_cleaner(self, cleaner):
        self._cleaner = cleaner

    @staticmethod
    def get_coordinate_point(cleaner, environment):
        grids = environment.grids()
        x, y = cleaner.position()
        max_index = len(grids) - 1
        return max_index - y, x
