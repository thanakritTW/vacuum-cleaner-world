import unittest

from game.environment import Environment


class EnvironmentTestCase(unittest.TestCase):

    def setUp(self):
        self.environment = Environment()

    def test_should_return_default_simple_grids(self):
        expected = [
            [0,0,0,0,1],
            [0,1,0,0,1],
            [0,0,1,0,1],
            [0,0,0,0,1],
            [0,0,1,0,1],
        ]

        grids = self.environment.grids()

        self.assertEqual(grids, expected)
