import unittest

from game.environment import Environment


class EnvironmentTestCase(unittest.TestCase):

    def setUp(self):
        self.environment = Environment()

    def test_should_return_default_simple_grids(self):
        expected = [
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1],
        ]

        grids = self.environment.grids()

        self.assertEqual(grids, expected)

    def test_should_return_input_grids(self):
        expected = [
            [0, 1],
            [1, 0],
        ]
        environment = Environment(expected)

        grids = environment.grids()

        self.assertEqual(grids, expected)

    def test_should_set_and_get_home(self):
        home = (1, 1)

        self.environment.set_home(home)

        self.assertEqual(self.environment.home(), home)

    def test_should_set_and_get_grids(self):
        grids = [[1, 0], [1, 0]]

        self.environment.set_grids(grids)

        self.assertEqual(self.environment.grids(), grids)