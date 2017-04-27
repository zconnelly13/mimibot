Contributing
============

This is a tutorial on adding a command to mimibot. In this tutorial we'll add 
a command called "ping" that just responds with "pong". This way it should be
clear what sort of "boiler plate" code is needed and it should be clear where
one would put the logic for an actual command.

### Prerequisites

Make sure you've already followed the installation instructions in the README

### Tests First

Don't be mad. But I'm going to really try to push TDD on you during this
tutorial. This repo is actually a really great example of where TDD is
strong. Commands are inherintly (mostly) functional in nature and most
of them are fairly simple.

Fire up your favorite editor and put this in `tests/ping.py`

```python
from unittest import TestCase

from mimibot.src.commands.ping import Ping


class TestPing(TestCase):
    def setUp(self):
        self.ping_command = Ping()

    def test_responds_with_pong(self):
        response = self.ping_command.get_response("ping")
        self.assertEqual(response, "pong")
```

Now run the tests. You should see an error to the effect of 
`no module named Ping` -- great!

This should look like your average python test for the most part. The curious
bits are as follows.

```python
# a command is an object that inherits from Object 
# (we'll see more of this in a bit)
self.ping_command = Ping()

# It should implement a method called `get_response` that takes one argument
# and two kwargs (user and channel)
response = self.ping_command.get_response("ping")
```

Things will make a bit more sense in a moment.

### Now the Implementation

```python
class Ping(object):
    def __init__(self):
        self.command = "ping"
        self.help_text = "responds with 'pong'"
        self.usage = "ping"

    def get_response(self, command, user=None, channel=None):
        if command.startswith(self.command):
            return "pong"
```

and a brief explanation

```python
# self.command is the word that will trigger this command
self.command = "ping"

# self.help_text is what's displayed when a user says
# "@mimibot help" or "@mimibot help <command>"
self.help_text = "responds with 'pong'"


# self.usage is an example of how to use the command
# like "add 1 2" or "deploy hearingtest staging"
self.usage = "ping"

    
# finally `get_response` contains all the logic for deciding
# how the bot will respond.
def get_response(self, command, user=None, channel=None):
    if command.startswith(self.command):
        return "pong"
```

Run the tests again and we should be green!

### Registering the Command

The last annoying little bit that needs to be done is adding the new command
to the registry. This is necessary because I, the maintainer, am skeptical
and a little scared of using too much python metaclass magic.

Edit `src/registry.py` to include the new `Ping` command in alphabetical order

```python
# ... imports
from mimibot.src.commands.ping import Ping
# ... more imports

COMMANDS = [
    # ...
    Ping(),
    # ...
]
```

### Make Chat

You can test your changes locally by running `make chat`

```bash
zac@macbook ~/personal_projects/mimibot $ make chat
PYTHONPATH='..' python src/chat.py
Chat with mimibot below

@mimibot ping
pong

@mimibot 
```

Looks good to me

### You're Done! (sort of)

Now you have a working command -- great! Make a PR.

Once your PR is merged into master it'll be automatically deployed and live
