class Environment:

    def __init__(self, grids=[
            [0,0,0,0,1],
            [0,1,0,0,1],
            [0,0,1,0,1],
            [0,0,0,0,1],
            [0,0,1,0,1],
        ]):
        self._grids = grids

    def grids(self):
        return self._grids
