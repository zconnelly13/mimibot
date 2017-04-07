import os

test = os.environ.get("MIMIBOT_TEST")
if test:
    DB_PATH = './.test.db'
else:
    DB_PATH = './db/pickle.db'
