import unittest
from unittest.mock import Mock, MagicMock

from game.sensors.touch_sensor import TouchSensor


class TouchSensorTestCase(unittest.TestCase):

    def setUp(self):
        self.environment = Mock()
        self.environment.grids = MagicMock(return_value=[
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 1],
        ])
        self.cleaner = Mock()
        self.touch_sensor = TouchSensor(self.cleaner, self.environment)

    def test_should_return_one_on_run_when_cleaner_hits_the_walls(self):
        self.run_test_with(position_after_try_to_move=(-1, 0), expected=1)
        self.run_test_with(position_after_try_to_move=(0, -1), expected=1)

        self.run_test_with(position_after_try_to_move=(0, 3), expected=1)
        self.run_test_with(position_after_try_to_move=(3, 0), expected=1)

    def test_should_return_zero_on_run_when_cleaner_does_not_hit_the_walls(self):
        self.run_test_with(position_after_try_to_move=(0, 0), expected=0)
        self.run_test_with(position_after_try_to_move=(2, 2), expected=0)

    def run_test_with(self, position_after_try_to_move, expected):
        cleaner_after_try_to_move = Mock()
        self.cleaner.act = MagicMock(return_value=cleaner_after_try_to_move)
        cleaner_after_try_to_move.position = MagicMock(return_value=position_after_try_to_move)

        result = self.touch_sensor.run()

        self.assertEqual(result, expected)
