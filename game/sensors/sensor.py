class BasedSensor:

    def __init__(self, cleaner, environment):
        self._cleaner = cleaner
        self._environment = environment

    def set_cleaner(self, cleaner):
        self._cleaner = cleaner
