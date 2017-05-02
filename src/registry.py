from mimibot.src.commands.add import Add
from mimibot.src.commands.get import Get
from mimibot.src.commands.help import Help
from mimibot.src.commands.linkme import Linkme
from mimibot.src.commands.set import Set
from mimibot.src.commands.translate import Translate
from mimibot.src.commands.ubersetzen import Ubersetzen

COMMANDS = [
    Add(),
    Get(),
    Help(),
    Linkme(),
    Set(),
    Translate(),
    Ubersetzen(),
]
