import unittest
from unittest.mock import Mock, MagicMock

from game.engine import Engine


class EngineTestCase(unittest.TestCase):

    def setUp(self):
        self.environment = Mock()
        self.environment.grids = MagicMock(return_value=[
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1],
        ])
        self.cleaner = Mock()
        self.touch_sensor = Mock()
        self.photo_sensor = Mock()
        self.infrared_sensor = Mock()
        self.engine = Engine(
            self.cleaner, self.environment, self.touch_sensor, self.photo_sensor, self.infrared_sensor,
        )

    def test_should_act_when_action_is_pushed(self):
        next_cleaner = Mock()
        self.cleaner.act = MagicMock(return_value=next_cleaner)

        self.engine.push_action("go_forward")

        self.cleaner.act.assert_called_with("go_forward")
        self.assertEqual(self.engine._latest_cleaner, next_cleaner)
        self.assertIn(next_cleaner, self.engine._history)

    def test_should_call_sensors_to_retrieve_information(self):
        self.touch_sensor.run = MagicMock(return_value=1)
        self.photo_sensor.run = MagicMock(return_value=0)
        self.infrared_sensor.run = MagicMock(return_value=1)

        results = self.engine.sensors()

        self._assertSensors(results, (1, 0, 1))

    def _assertSensors(self, results, expectations):
        touch_sensor, photo_sensor, infrared_sensor = results
        self.assertEqual(touch_sensor, expectations[0])
        self.assertEqual(photo_sensor, expectations[1])
        self.assertEqual(infrared_sensor, expectations[2])