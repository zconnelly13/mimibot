import os
import requests
import json

from mimibot.src.constants import GOOGLE_TRANSLATE_URL


class Translate(object):
    def __init__(self):
        self.command = "translate"
        self.help_text = "translates text from english to german"
        self.usage = "translate Hello, I am a human."

    def get_response(self, command, user=None, channel=None):
        if command.startswith(self.command):
            return self.translate(" ".join(command.split(" ")[1:]))

    def translate(self, query):
        parameters = {
            'key': os.environ.get('GOOGLE_TRANSLATE_API_KEY'),
            'q': query,
            'source': 'en',
            'target': 'de',
        }
        response = requests.get(GOOGLE_TRANSLATE_URL.format(**parameters))
        translation = json.loads(response.content)
        translated = (
            translation['data']['translations'][0]['translatedText'])
        return translated
