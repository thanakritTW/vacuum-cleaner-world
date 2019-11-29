import unittest

from game.cleaner import Cleaner


class CleanerTestCase(unittest.TestCase):

    def setUp(self):
        self.cleaner = Cleaner()

    def test_should_set_position_and_derection_via_constructor(self):
        cleaner = Cleaner((1, 1), 90)
        self.assertEqual(cleaner.position(), (1, 1))
        self.assertEqual(cleaner.direction(), 90)

    def test_cleaner_should_have_five_actions(self):
        actions = self.cleaner._actions

        self.assertIn("clean", actions)
        self.assertIn("turn_off", actions)
        self.assertIn("go_forward", actions)
        self.assertIn("turn_left", actions)
        self.assertIn("turn_right", actions)

    def test_should_raise_if_invalid_action(self):
        with self.assertRaises(Exception):
            self.cleaner.act("invalid_action")

    def test_should_return_new_instance_if_action_is_valid(self):
        valid_action = "valid_action"
        self.cleaner._actions.append(valid_action)

        cleaner = self.cleaner.act(valid_action)

        self.assertIsInstance(cleaner, Cleaner)

    def test_should_start_with_position_0_0(self):
        self.assertEqual(self.cleaner.position(), (0,0))

    def test_should_start_with_direction_positive_x(self):
        self.assertEqual(self.cleaner.direction(), 0)

    def test_should_move_forward_when_go_forward(self):
        action = "go_forward"

        self.cleaner._direction = 0
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.position(), (1,0))

        self.cleaner._direction = 90
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.position(), (0,1))

        self.cleaner._direction = 180
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.position(), (-1,0))

        self.cleaner._direction = 270
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.position(), (0,-1))

    def test_should_turn_left_when_turn_left(self):
        action = "turn_left"

        self.cleaner._direction = 0
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.direction(), 90)

        self.cleaner._direction = 90
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.direction(), 180)

        self.cleaner._direction = 180
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.direction(), 270)

        self.cleaner._direction = 270
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.direction(), 0)

    def test_should_turn_right_when_turn_right(self):
        action = "turn_right"

        self.cleaner._direction = 0
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.direction(), 270)

        self.cleaner._direction = 270
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.direction(), 180)

        self.cleaner._direction = 180
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.direction(), 90)

        self.cleaner._direction = 90
        cleaner = self.cleaner.act(action)
        self.assertEqual(cleaner.direction(), 0)