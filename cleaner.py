import math

class Cleaner:
    _actions = ["clean", "turn_left", "turn_right", "go_forward", "turn_off"]

    def __init__(self):
        self._position = (0,0)
        self._direction = 0

    def act(self, action):
        if action not in self._actions:
            raise Exception("Invalid move")

        if action == "go_forward":
            self._go_forward()

        if action == "turn_left":
            self._turn_left()

        if action == "turn_right":
            self._turn_right()

        return True

    def _go_forward(self):
        x, y = self._position[0], self._position[1]
        rad = math.radians(self._direction)
        self._position = (int(x + math.cos(rad)), int(y + math.sin(rad)))

    def _turn_right(self):
        self._direction = self._direction + 90
        if (self._direction >= 360):
            self._direction -= 360

    def _turn_left(self):
        self._direction = self._direction - 90
        if (self._direction < 0):
            self._direction += 360


