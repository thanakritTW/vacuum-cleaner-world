import unittest
from unittest.mock import Mock, MagicMock

from game.sensors.photo_sensor import PhotoSensor


class PhotoSensorTestCase(unittest.TestCase):

    def setUp(self):
        self.environment = Mock()
        self.environment.grids = MagicMock(return_value=[
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 1],
        ])
        self.cleaner = Mock()
        self.photo_sensor = PhotoSensor(self.cleaner, self.environment)

    def test_should_return_one_when_there_is_dirt(self):
        self.cleaner.position = MagicMock(return_value=(2, 2))

        result = self.photo_sensor.run()

        self.assertEqual(result, 1)

    def test_should_return_zero_when_there_is_no_dirt(self):
        self.cleaner.position = MagicMock(return_value=(0, 0))

        result = self.photo_sensor.run()

        self.assertEqual(result, 0)
