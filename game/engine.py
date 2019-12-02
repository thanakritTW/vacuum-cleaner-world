from game.service import UtilService


class Engine:
    def __init__(self, cleaner, environment, touch_sensor, photo_sensor, infrared_sensor):
        self._latest_cleaner = cleaner
        self._history = [cleaner]
        self._environment = environment
        self._environment.set_home(cleaner.position())

        self._touch_sensor = touch_sensor
        self._photo_sensor = photo_sensor
        self._infrared_sensor = infrared_sensor

        self._score = 0

    def push_action(self, action):
        if action == "clean":
            self._clean()
        next_cleaner = self._latest_cleaner.act(action)
        self._update_cleaner(next_cleaner)
        self._reduce_score_after_action()

    def _reduce_score_after_action(self):
        self._score = self._score - 1

    def sensors(self):
        return self._touch_sensor.run(), self._photo_sensor.run(), self._infrared_sensor.run()

    def score(self):
        return self._score

    def _clean(self):
        i, j = UtilService.get_coordinate_point(self._latest_cleaner, self._environment)
        grids = self._environment.grids()
        if grids[i][j] == 1:
            self._get_score_after_clean()
            grids[i][j] = 0
            self._environment.set_grids(grids)

    def _get_score_after_clean(self):
        self._score = self._score + 100

    def _update_cleaner(self, cleaner):
        self._latest_cleaner = cleaner

        self._touch_sensor.set_cleaner(cleaner)
        self._photo_sensor.set_cleaner(cleaner)
        self._infrared_sensor.set_cleaner(cleaner)

        self._history.append(cleaner)
