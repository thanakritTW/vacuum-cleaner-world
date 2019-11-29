import unittest
from unittest.mock import Mock, MagicMock

from game.engine import Engine


class EngineTestCase(unittest.TestCase):

    def setUp(self):
        self.environment = Mock()
        self.environment.grids = MagicMock(return_value=[
            [0,0,0,0,1],
            [0,1,0,0,1],
            [0,0,1,0,1],
            [0,0,0,0,1],
            [0,0,1,0,1],
        ])
        self.cleaner = Mock()
        self.engine = Engine(self.cleaner, self.environment)

    def test_should_return_one_on_get_touch_sensor(self):
        went_forward_cleaner = Mock()
        went_forward_cleaner.position = MagicMock(return_value=(-1, 0))
        self.cleaner.act = MagicMock(return_value=went_forward_cleaner)

        result = self.engine.touch_sensor()

        self.assertEqual(result, 1)

    def test_should_return_zero_on_get_touch_sensor(self):
        went_forward_cleaner = Mock()
        went_forward_cleaner.position = MagicMock(return_value=(2, 3))
        self.cleaner.act = MagicMock(return_value=went_forward_cleaner)

        result = self.engine.touch_sensor()

        self.assertEqual(result, 0)

    def test_should_return_one_when_there_is_dirt(self):
        self.cleaner.position = MagicMock(return_value=(2, 2))

        result = self.engine.photosensor()

        self.assertEqual(result, 1)

    def test_should_return_zero_when_there_is_no_dirt(self):
        self.cleaner.position = MagicMock(return_value=(0, 0))

        result = self.engine.photosensor()

        self.assertEqual(result, 0)

    def test_should_return_one_on_bumped_to_wall_an_zeros_for_other(self):
        self.cleaner.position = MagicMock(return_value=(0, 0))
        self.cleaner.direction = MagicMock(return_value=180)

        results = self.engine.sensors()

        self._assertSensors(results, (1, 0, 0))

    def _assertSensors(self, results, expectations):
        touch_sensor, photosensor, infrared_sensor = results
        self.assertEqual(touch_sensor, expectations[0])
        self.assertEqual(photosensor, expectations[1])
        self.assertEqual(infrared_sensor, expectations[2])