from mimibot.src.db import db


class Get(object):
    def __init__(self):
        self.command = "get"
        self.help_text = "gets a key from the db"
        self.usage = "get foo"
        self.db = db

    def get_response(self, command, user=None, channel=None):
        if command.startswith(self.command):
            key = command.split(" ")[1]
            val = db.get(key)
            return "%s: %s" % (key, val)
