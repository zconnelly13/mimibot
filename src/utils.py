import os
import requests
import json

from mimibot.src.constants import GOOGLE_TRANSLATE_URL


def translate(query, source, target):
    parameters = {
        'key': os.environ.get('GOOGLE_TRANSLATE_API_KEY'),
        'q': query,
        'source': source,
        'target': target,
    }
    response = requests.get(GOOGLE_TRANSLATE_URL.format(**parameters))
    translation = json.loads(response.content)
    translated = (
        translation['data']['translations'][0]['translatedText'])
    return translated
