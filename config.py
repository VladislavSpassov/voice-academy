import os
from slack_sdk import WebClient

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

def get_slack_client():
    client = WebClient(token=SLACK_BOT_TOKEN)
    return client

