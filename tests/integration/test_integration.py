import unittest

from game.cleaner import Cleaner
from game.environment import Environment
from game.engine import Engine
from game.sensors.infrared_sensor import InfraredSensor
from game.sensors.photo_sensor import PhotoSensor
from game.sensors.touch_sensor import TouchSensor


class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        cleaner = Cleaner(position=(1, 1), direction=90)
        environment = Environment([
            [1, 0],
            [0, 1],
        ])
        touch_sensor = TouchSensor(cleaner, environment)
        photo_sensor = PhotoSensor(cleaner, environment)
        infrared_sensor = InfraredSensor(cleaner, environment)
        self.engine = Engine(cleaner, environment, touch_sensor, photo_sensor, infrared_sensor)

    def test_cleaner_clean_up(self):
        self.engine.push_action("turn_left")
        self.engine.push_action("go_forward")
        self.engine.push_action("clean")
        self._assertSensors((1, 0, 0))

        self.engine.push_action("turn_left")
        self.engine.push_action("go_forward")
        self.engine.push_action("turn_left")
        self.engine.push_action("go_forward")
        self.engine.push_action("clean")
        self._assertSensors((1, 0, 0))

        self.assertEqual(self.engine._environment.grids(), [
            [0, 0],
            [0, 0]
        ])

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
