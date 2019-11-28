import unittest

from game.environment import Environment


class EnvironmentTestCase(unittest.TestCase):

    def setUp(self):
        self.environment = Environment()