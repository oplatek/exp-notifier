# Experiment Notifier

## Usage 

```
ntf --channel exp-notifier --text "Your text goes here"
```

## Development

```
# change to git root directory of source code
pip install -e .
```

## Installation
- [Setup and install the app](https://api.slack.com/start/building/bolt-python#start)
  - Set permissions/scopes to `chat:write`, `identityb:basic`,`groups:write`, `im:write`
  - Remember `SLACK_BOT_TOKEN`
- [Setup Socket mode](https://api.slack.com/apis/connections/socket#sdks). 
  - Remember `SLACK_APP_TOKEN` 
- Add your app `APPNAME e.g. exp-notifier`  to slack channel `#CHANNEL e.g. #exp-notifier`
- Install the CLI client locally. See [Development](#development)
