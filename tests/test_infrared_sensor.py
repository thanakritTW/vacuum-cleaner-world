import unittest
from unittest.mock import Mock, MagicMock

from game.sensors.infrared_sensor import InfraredSensor


class InfraredSensorTestCase(unittest.TestCase):

    def setUp(self):
        self.environment = Mock()
        self.environment.grids = MagicMock(return_value=[
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 1],
        ])
        self.cleaner = Mock()
        self.infrared_sensor = InfraredSensor(self.cleaner, self.environment)

    def test_should_return_one_when_it_is_home_position(self):
        self.cleaner.position = MagicMock(return_value=(2, 2))
        self.environment.home = MagicMock(return_value=(2, 2))

        result = self.infrared_sensor.run()

        self.assertEqual(result, 1)

    def test_should_return_zero_when_it_is_not_home_position(self):
        self.cleaner.position = MagicMock(return_value=(0, 0))
        self.environment.home = MagicMock(return_value=(2, 2))

        result = self.infrared_sensor.run()

        self.assertEqual(result, 0)

