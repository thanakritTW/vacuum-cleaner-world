import unittest

from game.cleaner import Cleaner
from game.environment import Environment
from game.engine import Engine


class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.cleaner = Cleaner(position=(1, 1), direction=90)
        self.environment = Environment([
            [1,0],
            [0,1],
        ])
        self.engine = Engine(self.cleaner, self.environment)

    def test_simple_program_flow_cleaner_move(self):
        self._assertSensors((1, 0, 1))

        self.engine.push_action("turn_left")
        self._assertSensors((0, 0, 1))

        self.engine.push_action("go_forward")
        self._assertSensors((1, 1, 0))

        self.engine.push_action("turn_right")
        self._assertSensors((1, 1, 0))

        self.engine.push_action("turn_right")
        self._assertSensors((0, 1, 0))

        self.engine.push_action("turn_right")
        self._assertSensors((0, 1, 0))

    def _assertSensors(self, expecteds):
        self.assertEqual(self.engine.touch_sensor(), expecteds[0])
        self.assertEqual(self.engine.photosensor(), expecteds[1])
        self.assertEqual(self.engine.infrared_sensor(), expecteds[2])
