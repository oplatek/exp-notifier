import logging
import os
from pathlib import Path


logger = logging.getLogger(__name__)

def get_slack_bot_token(token_var=None, token_file=None):
    os.environ.get("SLACK_BOT_TOKEN")
    SLACK_BOT_TOKEN_FILENAME = Path('.slack_bot_token')
    if SLACK_BOT_TOKEN_FILENAME.is_file() and token_file is None:  # in current working directory
        token_file = SLACK_BOT_TOKEN_FILENAME
    token_file = token_file if token_file is not  None \
            else Path(os.environ['HOME'])  / SLACK_BOT_TOKEN_FILENAME
    if token_file.is_file():
        with open(token_file, 'rt') as r:
            return r.read().strip()
    else:
        logger.warn(f'{token_file} file does not exists.\nCannot use safer way of loading tokens from file for slack bot token.')
        token_var = token_var if token_var is not None else 'SLACK_BOT_TOKEN'
        logger.warn(f'Loading slack bot token from {token_var} variable.')
        return os.environ[token_var].strip()
