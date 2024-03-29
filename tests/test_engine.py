import unittest
from unittest.mock import Mock, MagicMock

from game.engine import Engine


class EngineTestCase(unittest.TestCase):

    def setUp(self):
        self.cleaner = Mock()
        self.cleaner.position = MagicMock(return_value=(1, 1))

        self.environment = Mock()

        self.touch_sensor = Mock()
        self.photo_sensor = Mock()
        self.infrared_sensor = Mock()

        self.engine = Engine(
            self.cleaner, self.environment, self.touch_sensor, self.photo_sensor, self.infrared_sensor,
        )

    def test_should_get_score(self):
        score = self.engine.score()

        self.assertEqual(score, 0)

    def test_should_lose_score_when_take_action(self):
        self.engine.push_action("go_forward")

        score = self.engine.score()

        self.assertEqual(score, -1)

    def test_should_get_score_when_successfully_clean_up(self):
        self.cleaner.position = MagicMock(return_value=(1, 1))
        self.environment.grids = MagicMock(return_value=[
            [1, 1],
            [0, 1],
        ])
        self.engine.push_action("clean")

        score = self.engine.score()

        self.assertEqual(score, 100 - 1)

    def test_should_do_nothing_and_terminate_when_turn_off_at_the_home_location(self):
        self.environment.home = MagicMock(return_value=(1, 1))
        self.cleaner.position = MagicMock(return_value=(1, 1))

        self.engine.push_action("turn_off")
        score = self.engine.score()

        self.assertEqual(score, -1)

    def test_should_reduce_score_and_terminate_when_turn_off_at_the_different_location(self):
        self.engine.push_action("turn_off")
        self.environment.home = MagicMock(return_value=(2, 2))
        self.cleaner.position = MagicMock(return_value=(1, 1))

        score = self.engine.score()

        self.assertEqual(score, - 1000 - 1)

    def test_should_not_get_score_when_clean_up_empty_tile(self):
        self.cleaner.position = MagicMock(return_value=(0, 0))
        self.environment.grids = MagicMock(return_value=[
            [1, 1],
            [0, 1],
        ])
        self.engine.push_action("clean")

        score = self.engine.score()

        self.assertEqual(score, -1)

    def test_should_set_home_when_engine_init(self):
        home_position = (1, 1)
        self.cleaner.position = MagicMock(return_value=home_position)
        environment = Mock()

        Engine(
            self.cleaner, environment, self.touch_sensor, self.photo_sensor, self.infrared_sensor,
        )

        environment.set_home.assert_called_once_with(home_position)

    def test_should_act_and_update_when_move(self):
        next_cleaner = Mock()
        self.cleaner.act = MagicMock(return_value=next_cleaner)

        self.engine.push_action("go_forward")

        self.cleaner.act.assert_called_with("go_forward")
        self.assertEqual(self.engine._latest_cleaner, next_cleaner)
        self.touch_sensor.set_cleaner.assert_called_with(next_cleaner)
        self.photo_sensor.set_cleaner.assert_called_with(next_cleaner)
        self.infrared_sensor.set_cleaner.assert_called_with(next_cleaner)
        self.assertIn(next_cleaner, self.engine._history)

    def test_should_call_sensors_to_retrieve_information(self):
        self.touch_sensor.run = MagicMock(return_value=1)
        self.photo_sensor.run = MagicMock(return_value=0)
        self.infrared_sensor.run = MagicMock(return_value=1)

        results = self.engine.sensors()

        self._assertSensors(results, (1, 0, 1))

    def test_should_clean_room_and_set_new_grids(self):
        self.cleaner.position = MagicMock(return_value=(1, 1))
        self.environment.grids = MagicMock(return_value=[
            [1, 1],
            [0, 1],
        ])

        self.engine.push_action("clean")

        self.environment.set_grids.assert_called_once_with([
            [1, 0],
            [0, 1],
        ])

    def _assertSensors(self, results, expectations):
        touch_sensor, photo_sensor, infrared_sensor = results
        self.assertEqual(touch_sensor, expectations[0])
        self.assertEqual(photo_sensor, expectations[1])
        self.assertEqual(infrared_sensor, expectations[2])