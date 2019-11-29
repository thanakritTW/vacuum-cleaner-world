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

    def test_should_act_when_action_is_pushed(self):
        went_forward_cleaner = Mock()
        went_forward_cleaner.position = MagicMock(return_value=(1, 1))
        self.cleaner.act = MagicMock(return_value=went_forward_cleaner)

        self.engine.push_action("go_forward")

        self.cleaner.act.assert_called_with("go_forward")
        self.assertEqual(self.engine._latest_cleaner, went_forward_cleaner)
        self.assertIn(went_forward_cleaner, self.engine._history)

    def test_should_return_one_on_get_touch_sensor_hit_the_walls(self):
        went_forward_cleaner = Mock()
        self.cleaner.act = MagicMock(return_value=went_forward_cleaner)

        went_forward_cleaner.position = MagicMock(return_value=(-1, 0))
        result = self.engine.touch_sensor()
        self.assertEqual(result, 1)

        went_forward_cleaner.position = MagicMock(return_value=(0, -1))
        result = self.engine.touch_sensor()
        self.assertEqual(result, 1)

        went_forward_cleaner.position = MagicMock(return_value=(6, 0))
        result = self.engine.touch_sensor()
        self.assertEqual(result, 1)

        went_forward_cleaner.position = MagicMock(return_value=(0, 6))
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

    def test_should_return_one_when_it_is_home_position(self):
        self.cleaner.position = MagicMock(return_value=(2, 2))
        self.engine._home_position = (2, 2)

        result = self.engine.infrared_sensor()

        self.assertEqual(result, 1)

    def test_should_return_zero_when_it_is_not_home_position(self):
        self.cleaner.position = MagicMock(return_value=(0, 0))
        self.engine._home_position = (1, 1)

        result = self.engine.infrared_sensor()

        self.assertEqual(result, 0)

    def test_should_return_one_on_bumped_to_wall_and_zeros_for_other(self):
        self.cleaner.position = MagicMock(return_value=(0, 0))
        self.cleaner.direction = MagicMock(return_value=180)
        went_forward_cleaner = Mock()
        went_forward_cleaner.position = MagicMock(return_value=(-1, 0))
        self.cleaner.act = MagicMock(return_value=went_forward_cleaner)
        self.engine._home_position = (0, 0)

        results = self.engine.sensors()

        self._assertSensors(results, (1, 0, 1))

    def _assertSensors(self, results, expectations):
        touch_sensor, photosensor, infrared_sensor = results
        self.assertEqual(touch_sensor, expectations[0])
        self.assertEqual(photosensor, expectations[1])
        self.assertEqual(infrared_sensor, expectations[2])