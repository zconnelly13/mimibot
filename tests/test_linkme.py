from unittest import TestCase

from mimibot.src.commands.linkme import Linkme


class TestLinkme(TestCase):
    def setUp(self):
        self.linkme_command = Linkme()

    def test_responds(self):
        response = self.linkme_command.get_response("linkme")
        self.assertIsNotNone(response)

    def test_format_list_of_links(self):
        formatted = self.linkme_command.format_links(
            [
             ("Github", "http://github.com"),
             ("Google", "http://google.com"),
            ]
        )
        self.assertIn("*Github*", formatted)
        self.assertIn("http://github.com", formatted)
        self.assertIn("*Google*", formatted)
        self.assertIn("http://google.com", formatted)
