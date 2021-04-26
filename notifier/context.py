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
        self._postman('\n'.join(self._msgs))


class SlackMessage(Message):
    def __init__(self, postman=None, **kwargs):
        super().__init__()

        if postman is not None:
            if isinstance(postman, SlackMsgSend):
                self._postman = postman
            else:
                raise RuntimeError('When using class SlackPostmanMixin, you should provide SlackMsgSend instance as a postman')
        else:
            self._postman = SlackMsgSend(**kwargs)
