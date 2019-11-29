class Environment:

    def __init__(self, grids=None):
        if grids is None:
            grids = [
                [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 1, 0, 1],
            ]
        self._grids = grids
        self._home = None

    def grids(self):
        return self._grids

    def set_grids(self, grids):
        self._grids = grids

    def home(self):
        return self._home

    def set_home(self, home):
        self._home = home
