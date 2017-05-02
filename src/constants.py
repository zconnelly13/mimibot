import os

test = os.environ.get("MIMIBOT_TEST")
if test:
    DB_PATH = '/.test.db'
else:
    DB_PATH = '/db/pickle.db'

GOOGLE_TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2?key={key}&q={q}&source={source}&target={target}"  # noqa
