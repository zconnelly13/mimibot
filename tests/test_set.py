from unittest import TestCase

from mimibot.src.commands.set import Set
from mimibot.src.db import db


class TestSet(TestCase):
    def setUp(self):
        self.set_command = Set()

    def test_sets_a_value(self):
        self.set_command.get_response("set foo bar")
        self.assertEqual(db.get("foo"), "bar")
