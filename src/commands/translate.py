from mimibot.src.utils import translate


class Translate(object):
    def __init__(self):
        self.command = "translate"
        self.help_text = "translates text from english to german"
        self.usage = "translate Hello, I am a human."

    def get_response(self, command, user=None, channel=None):
        if command.startswith(self.command):
            return translate(" ".join(command.split(" ")[1:]), 'en', 'de')
