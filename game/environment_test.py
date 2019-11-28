import unittest

from game.environment import Environment


class TestCleaner(unittest.TestCase):

    def setUp(self):
        self.environment = Environment()