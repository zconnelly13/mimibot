from unittest import TestCase

import vcr

from mimibot.src.commands.ubersetzen import Ubersetzen


class TestUbersetzen(TestCase):
    def setUp(self):
        self.ubersetzen_command = Ubersetzen()

    @vcr.use_cassette(
        'tests/cassettes/test_ubersetzen_one_word',
        filter_query_parameters=['key'])
    def test_ubersetzen_one_word(self):
        response = self.ubersetzen_command.get_response("ubersetzen Katze")
        self.assertEqual(response, "cat")

    @vcr.use_cassette(
        'tests/cassettes/test_ubersetzen_many_words',
        filter_query_parameters=['key'])
    def test_ubersetzen_many_words(self):
        response = self.ubersetzen_command.get_response(
            "ubersetzen Ich bin eine Katze")
        self.assertEqual(response, "I am a cat")
