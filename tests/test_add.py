from unittest import TestCase

from mimibot.src.commands.add import Add


class TestAdd(TestCase):
    def setUp(self):
        self.add_command = Add()

    def test_adds_two_numbers(self):
        response = self.add_command.get_response("add 1 2", "channelfoo")
        self.assertEqual(3, response)

    def test_adds_more_than_two_numbers(self):
        response = self.add_command.get_response("add 1 2 3", "channelfoo")
        self.assertEqual(6, response)

    def test_responds_only_to_add(self):
        response = self.add_command.get_response("1 2", "channelfoo")
        self.assertIsNone(response)

        response = self.add_command.get_response("subtract 1 2", "channelfoo")
        self.assertIsNone(response)
