#!/usr/bin/env python3
import logging

import click 
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from notifier.slack import get_slack_bot_token

@click.command()
@click.option('--channel', required=True, type=str)
@click.option('--text', required=True, type=str)
def send_msg_to_channel(channel, text):
    client = WebClient(token=get_slack_bot_token())
    logger = logging.getLogger(__name__)

    try:
        result = client.chat_postMessage(
            channel=channel,
            text=text
        )
        logger.info(result)
    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")


if __name__ == "__main__":
    send_msg_to_channel()
