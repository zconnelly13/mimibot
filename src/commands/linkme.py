class Linkme(object):
    def __init__(self):
        self.command = "linkme"
        self.help_text = "Display a list of helpful links for mimi"
        self.usage = "@mimibot linkme"
        self.links = [
            ("Asana", "https://app.asana.com/"),
            ("Jira", "https://gomimi.atlassian.net/"),
            ("Web Hearing Test", "https://mimihearingtechnologies.github.io/web-hearingtest/"),  # nopep8
        ]

    def get_response(self, command, channel):
        if command.startswith(self.command):
            return self.format_links(self.links)

    def format_links(self, links):
        line = "*{0}* - {1}"
        formatted_links = [line.format(*link) for link in links]
        return "\n".join(formatted_links)
