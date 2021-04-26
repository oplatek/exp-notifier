import os
# Use the package we installed
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and signing secret
app = App(
        token=os.environ.get("SLACK_BOT_TOKEN"),
    )


@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")


@app.event("app_mention")
def event_test(say):
    say("Hi there!")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
