import unittest

import cleaner


class TestCleaner(unittest.TestCase):

    def setUp(self):
        self.cleaner = cleaner.Cleaner()

    def test_cleaner_should_have_five_actions(self):
        actions = self.cleaner.getActions()

        self.assertIn("clean", actions)
