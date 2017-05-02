from mimibot.src.utils import translate


class Ubersetzen(object):
    def __init__(self):
        self.command = "ubersetzen"
        self.help_text = "translates text from german to english"
        self.usage = "ubersetzen Hello, I am a cat."

    def get_response(self, command, user=None, channel=None):
        if command.startswith(self.command):
            return translate(" ".join(command.split(" ")[1:]), 'de', 'en')
