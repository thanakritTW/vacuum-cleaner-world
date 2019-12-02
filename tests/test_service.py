import unittest
from unittest.mock import Mock, MagicMock

from game.service import UtilService


class UtilServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.cleaner = Mock()
        self.environment = Mock()
        self.environment.grids = MagicMock(return_value=[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ])
        self.service = UtilService()

    def test_should_get_correct_coordinate_point(self):
        self.cleaner.position = MagicMock(return_value=(2, 2))
        coordinate = self.service.get_coordinate_point(self.cleaner, self.environment)
        self.assertEqual(coordinate, (0, 2))

        self.cleaner.position = MagicMock(return_value=(0, 0))
        coordinate = self.service.get_coordinate_point(self.cleaner, self.environment)
        self.assertEqual(coordinate, (2, 0))

        self.cleaner.position = MagicMock(return_value=(2, 0))
        coordinate = self.service.get_coordinate_point(self.cleaner, self.environment)
        self.assertEqual(coordinate, (2, 2))

        self.cleaner.position = MagicMock(return_value=(0, 2))
        coordinate = self.service.get_coordinate_point(self.cleaner, self.environment)
        self.assertEqual(coordinate, (0, 0))
