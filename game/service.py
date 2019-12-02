class UtilService:

    @staticmethod
    def get_coordinate_point(cleaner, environment):
        grids = environment.grids()
        x, y = cleaner.position()
        max_index = len(grids) - 1
        return max_index - y, x
