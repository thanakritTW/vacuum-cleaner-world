class Environment:

    def __init__(self):
        self._grids = [
            [0,0,0,0,1],
            [0,1,0,0,1],
            [0,0,1,0,1],
            [0,0,0,0,1],
            [0,0,1,0,1],
        ]

    def grids(self):
        return self._grids
