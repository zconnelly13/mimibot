from unittest import TestCase

import vcr

from mimibot.src.commands.translate import Translate


class TestAdd(TestCase):
    def setUp(self):
        self.translate_command = Translate()

    @vcr.use_cassette(
        'tests/cassettes/test_translates_words',
        filter_query_parameters=['key'])
    def test_translates_words(self):
        response = self.translate_command.get_response("translate two")
        self.assertEqual(response, "zwei")

    @vcr.use_cassette(
        'tests/cassettes/test_translates_sentences',
        filter_query_parameters=['key'])
    def test_translates_sentences(self):
        response = self.translate_command.get_response(
            "translate Hello, I am a robot.")
        self.assertEqual(response, "Hallo, ich bin ein Roboter.")
