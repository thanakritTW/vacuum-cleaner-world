from game.sensors.sensor import BasedSensor


class InfraredSensor(BasedSensor):
    def __init__(self, cleaner, environment):
        super().__init__(cleaner, environment)

    def run(self):
        return int(self._environment.home() == self._cleaner.position())
