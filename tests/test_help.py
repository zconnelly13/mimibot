from unittest import TestCase

from mimibot.src.commands.help import Help


class TestHelp(TestCase):
    def setUp(self):
        self.help_command = Help()

    def test_runs_default(self):
        try:
            self.help_command.get_response("help")
        except Exception as e:
            self.fail(
                "Exception thrown trying to generate help text: %s" % str(e))

    def test_help_usage(self):
        response = self.help_command.get_response("help help")
        self.assertEqual(
            response,
            "*Usage:* @mimibot help or @mimibot help <command>")

    def test_format_help_text(self):
        help_text = self.help_command.format_help_text(self.help_command)
        self.assertEqual(help_text, '*help* - display help text')
