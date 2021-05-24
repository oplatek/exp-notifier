import logging
import os
from pathlib import Path
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


logger = logging.getLogger(__name__)

def get_slack_bot_token(token_var=None, token_file=None, **kwargs):
    SLACK_BOT_TOKEN_FILENAME = Path('.slack_bot_token')
    token_file = token_file if token_file is not  None \
            else Path(os.environ['HOME'])  / SLACK_BOT_TOKEN_FILENAME
    if token_file.is_file():
        with open(token_file, 'rt') as r:
            return r.read().strip()
    else:
        logger.warn(f'{token_file} file does not exists.\nCannot use safer way of loading tokens from file for slack bot token.')
        token_var = token_var if token_var is not None else 'SLACK_BOT_TOKEN'
        logger.warn(f'Loading slack bot token from {token_var} variable.')
        if not token_var in os.environ:
            logging.warn(f'Cannot get slack app token even from {token_var}')
            return ''
        else:
            return os.environ.get(token_var, '').strip()


def send_msg_to_channel(token, channel, text):
    logger = logging.getLogger(__name__)
    if channel == '/dev/null':
        logger.warn(f'Channel /dev/null. Dumping message:\n\n{text}\n')
        return

    client = WebClient(token=token)

    try:
        result = client.chat_postMessage(
            channel=channel,
            text=text
        )
        logger.info(result)
    except SlackApiError as e:
        logger.exception(f'Error posting message: {e}')


class SlackMsgSend:
    def __init__(self, msg=None, channel=None, token=None, **kwargs):
        self.channel = "" if channel is None else channel
        self.msg = "" if msg is None else msg
        self.token = get_slack_bot_token() if token is None else token
        assert self.channel, 'You need to specify channel'
        assert self.token, 'You need to specify token'

    def __call__(self, msg=None, append=True):
        msg = '' if msg is None else msg
        if append:
            self.msg += msg
        else:
            self.msg = msg
        send_msg_to_channel(self.token, self.channel, self.msg)
