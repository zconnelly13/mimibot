import os
import time

from slackclient import SlackClient

from mimibot.src.registry import COMMANDS

# starterbot's ID as an environment variable
MIMI_BOT_ID = os.environ.get("MIMI_BOT_ID")

# constants
AT_BOT = "<@" + MIMI_BOT_ID + ">"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('MIMI_BOT_TOKEN'))


def handle_message(message, user, channel):
    """
    Receives commands directed at the bot and determines if they
    are valid commands. If so, then acts on the commands. If not,
    returns back what it needs for clarification.
    """
    responses = [response for response in
                 [command.get_response(message, user=user, channel=channel) for
                  command in COMMANDS]
                 if response]
    for response in responses:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response,
            as_user=True)


def parse_slack_output(slack_rtm_output):
    """
    The Slack Real Time Messaging API is an events firehose.
    this parsing function returns None unless a message is
    directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['user'], output['channel']
    return None, None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("MimiBot connected and running!")
        while True:
            try:
                slack_read = slack_client.rtm_read()
                command, user, channel = parse_slack_output(slack_read)
                if command and channel:
                    handle_message(command, user, channel)
            except Exception as e:
                slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text="Oops! Something went wrong",
                    as_user=True)

            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
