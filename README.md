# Experiment Notifier

## Usage 

### Slack notifications
The experiment notifier assumes that for sending messages you have `SLACK_BOT_TOKEN` either in:
- current working directory stored in `./.slack_bot_token` file
- or at your home dir in the file `$HOME/.slack_bot_token`
- or in `SLACK_BOT_TOKEN` variable

Note, that storing the token in a file with `600` permissions is the recommended method.

```
# CLI usage
$ ntf --channel exp-notifier --text "Your text goes here"
```

```
# Python usage
from notifier.context import SlackMessage

with SlackMessage(channel='exp-notifier') as sm:
  sm.write('test from python')
```

## Installation
- [Setup and install the app](https://api.slack.com/start/building/bolt-python#start)
  - Set permissions/scopes to `chat:write`, `identityb:basic`,`groups:write`, `im:write`
  - Remember `SLACK_BOT_TOKEN`
- [Setup Socket mode](https://api.slack.com/apis/connections/socket#sdks). 
  - Remember `SLACK_APP_TOKEN` 
- Add your app `APPNAME e.g. exp-notifier`  to slack channel `#CHANNEL e.g. #exp-notifier`
- Install the CLI client locally. See [Development](#development)

## Development

```
# change to git root directory of source code
pip install -e .
```

## Features
- [x] Sending text message to a channel under the app name.
- [ ] Sending a text instant message (IM).
- [ ] Attach file (log file) to a message
- [ ] Attach a picture / sound file to be played back
- [ ] Send a text message and mention a person
- [ ] Block code execution, present poll to a user, continue based on the poll answer. 

Pull requests are welcome!
