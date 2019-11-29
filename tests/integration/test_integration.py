import unittest

from game.cleaner import Cleaner
from game.environment import Environment
from game.engine import Engine
from game.sensors.infrared_sensor import InfraredSensor
from game.sensors.photo_sensor import PhotoSensor
from game.sensors.touch_sensor import TouchSensor


class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.cleaner = Cleaner(position=(1, 1), direction=90)
        self.environment = Environment([
            [1, 0],
            [0, 1],
        ])
        self.touch_sensor = TouchSensor(self.cleaner, self.environment)
        self.photo_sensor = PhotoSensor(self.cleaner, self.environment)
        self.infrared_sensor = InfraredSensor(self.cleaner, self.environment)
        self.engine = Engine(self.cleaner, self.environment, self.touch_sensor, self.photo_sensor, self.infrared_sensor)

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

        self.engine.push_action("go_forward")
        self._assertSensors((1, 0, 0))

        self.engine.push_action("turn_left")
        self._assertSensors((0, 0, 0))

        self.engine.push_action("go_forward")
        self._assertSensors((1, 1, 0))

        self.engine.push_action("turn_left")
        self._assertSensors((0, 1, 0))

        self.engine.push_action("go_forward")
        self._assertSensors((1, 0, 1))

    def _assertSensors(self, expecteds):
        touch_sensor, photo_sensor, infrared_sensor = self.engine.sensors()
        self.assertEqual(touch_sensor, expecteds[0])
        self.assertEqual(photo_sensor, expecteds[1])
        self.assertEqual(infrared_sensor, expecteds[2])
