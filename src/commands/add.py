class Add(object):
    def __init__(self):
        self.command = "add"
        self.help_text = "adds one or more number(s) together"
        self.usage = "add 4 5"

    def get_response(self, command, channel):
        if not command.startswith(self.command):
            return None
        else:
            return sum(map(int, command.split(" ")[1:]))
