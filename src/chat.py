from mimibot.src.registry import COMMANDS


def handle_message(message):
    """
    Sees if the message provokes any responses from the bot.
    """
    responses = [response for response in
                 [command.get_response(message, "channel_foo") for
                  command in COMMANDS]
                 if response]
    for response in responses:
        print response
    print ""


if __name__ == "__main__":
    print "Chat with mimibot below"
    print ""
    while True:
        message = str(raw_input("@mimibot "))
        handle_message(message)
