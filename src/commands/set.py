from mimibot.src.db import db


class Set(object):
    def __init__(self):
        self.command = "set"
        self.help_text = "sets a key in the db"
        self.usage = "set foo bar"
        self.db = db

    def get_response(self, command, user=None, channel=None):
        if command.startswith(self.command):
            (key, val) = command.split(" ")[1:]
            db.set(key, val)
            db.dump()
            return "Cool, set %s to %s" % (key, val)
