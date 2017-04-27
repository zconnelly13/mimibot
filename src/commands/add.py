class Add(object):
    def __init__(self):
        self.command = "add"
        self.help_text = "adds one or more number(s) together"
        self.usage = "add 4 5"

    def get_response(self, command, user=None, channel=None):
        if command.startswith(self.command):
            return sum(map(int, command.split(" ")[1:]))
