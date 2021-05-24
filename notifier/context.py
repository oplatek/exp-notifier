import logging
from notifier.slack import SlackMsgSend

class LoggingPostman:
    def __init__(self):
        logging.warn('Using LoggingPostman which logs the messages using logging.info function.\n\tAdjust your logging level if you want to see the messages!')

    def __call__(self, msg=None):
        msg = '' if msg is None else msg
        logging.info(msg)


class Message:
    def __init__(self, postman=None, **kwargs):
        self._postman = LoggingPostman() if postman is None else postman
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

        if postman is not None:
            if isinstance(postman, SlackMsgSend):
                postman = postman
            else:
                raise RuntimeError('You should provide SlackMsgSend instance as a postman')
        else:
            try:
                postman = SlackMsgSend(**kwargs)
            except Exception as e:
                logging.exception('Cannot create a Slack postman. It is not possible to send messages to slack.')
        super().__init__(postman)
