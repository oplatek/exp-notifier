import logging
from notifier.slack import SlackMsgSend


class Message:
    def __init__(self, postman=None, **kwargs):
        self._postman = postman
        self._msgs = []

    def write(self, msg):
        self._msgs.append(msg)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        msg = '\n'.join(self._msgs)
        try:
            self._postman(msg)
        except Exception as e:
            logging.exception(f'FAIL sending message:\n\t{msg}\n\n')


class SlackMessage(Message):
    def __init__(self, postman=None, **kwargs):
        super().__init__()

        if postman is not None:
            if isinstance(postman, SlackMsgSend):
                self._postman = postman
            else:
                raise RuntimeError('You should provide SlackMsgSend instance as a postman')
        else:
            try:
                self._postman = SlackMsgSend(**kwargs)
            except Exception as e:
                logging.exception('Cannot create a Slack postman. It is not possible to send messages to slack.')
