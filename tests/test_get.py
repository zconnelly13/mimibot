from unittest import TestCase

from mimibot.src.commands.get import Get
from mimibot.src.db import db


class TestGet(TestCase):
    def setUp(self):
        self.get_command = Get()

    def test_sets_a_value(self):
        db.set("foo", "bar")
        response = self.get_command.get_response("get foo", "_")
        self.assertEqual(response, "foo: bar")
