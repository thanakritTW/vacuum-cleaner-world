class Engine:
    def __init__(self, cleaner, environment, touch_sensor, photo_sensor, infrared_sensor):
        self._latest_cleaner = cleaner
        self._history = [cleaner]
        self._environment = environment
        self._environment.set_home(cleaner.position())

        self._touch_sensor = touch_sensor
        self._photo_sensor = photo_sensor
        self._infrared_sensor = infrared_sensor

    def push_action(self, action):
        next_cleaner = self._latest_cleaner.act(action)
        self._latest_cleaner = next_cleaner

        self._touch_sensor.set_cleaner(next_cleaner)
        self._photo_sensor.set_cleaner(next_cleaner)
        self._infrared_sensor.set_cleaner(next_cleaner)

        self._history.append(next_cleaner)

    def sensors(self):
        return self._touch_sensor.run(), self._photo_sensor.run(), self._infrared_sensor.run()
