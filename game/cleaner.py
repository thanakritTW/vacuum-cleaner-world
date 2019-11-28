import math

class Cleaner:
    _actions = ["clean", "turn_left", "turn_right", "go_forward", "turn_off"]

    def __init__(self, position=(0,0), direction=0):
        self._position = position
        self._direction = direction

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

    def position(self):
        return self._position

    def direction(self):
        return self._direction

    def _go_forward(self):
        x, y = self._position[0], self._position[1]
        rad = math.radians(self._direction)
        new_position = (int(x + math.cos(rad)), int(y + math.sin(rad)))
        self._position = new_position

    def _turn_right(self):
        new_direction = self._direction + 90
        if (new_direction >= 360):
            new_direction -= 360
        self._direction = new_direction

    def _turn_left(self):
        new_direction = self._direction - 90
        if (new_direction < 0):
            new_direction += 360
        self._direction = new_direction


