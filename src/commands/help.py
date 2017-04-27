class Help(object):
    def __init__(self):
        self.command = "help"
        self.help_text = "display help text"
        self.usage = "@mimibot help or @mimibot help <command>"

    def get_response(self, command, user=None, channel=None):
        # avoid circular imports
        from mimibot.src.registry import COMMANDS
        if command == self.command:
            cmd_help_texts = [self.format_help_text(cmd)
                              for cmd in COMMANDS if cmd.command != "help"]
            cmd_help_text = "\n".join(cmd_help_texts)
            intro_help_text = "Here is a list of commands -- for usage instructions try 'help <command>'"  # noqa
            return intro_help_text + "\n\n" + cmd_help_text
        elif command.startswith(self.command):
            query_command = command.split(" ")[1]
            matched_help_text = [cmd for cmd in COMMANDS
                                 if cmd.command == query_command]
            if len(matched_help_text) == 1:
                cmd = matched_help_text[0]
                return "*Usage:* " + cmd.usage
            else:
                return None
        return None

    def format_help_text(self, cmd):
        return "*{command}* - {help_text}".format(
            command=cmd.command, help_text=cmd.help_text)
