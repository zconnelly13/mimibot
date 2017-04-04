class Help(object):
    def __init__(self):
        self.command = "help"
        self.help_text = "display help text"
        self.usage = "help"

    def get_response(self, command, channel):
        # avoid circular imports
        from mimibot.src.registry import COMMANDS
        if command.startswith(self.command):
            help_texts = [self.format_help_text(cmd)
                          for cmd in COMMANDS if cmd.command != "help"]
            help_text = "\n".join(help_texts)
            return help_text

    def format_help_text(self, cmd):
        return "*{command}* - {help_text}".format(
            command=cmd.command, help_text=cmd.help_text)
