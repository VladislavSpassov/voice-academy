from config import get_slack_client

def create_slack_channel(channel_name):
    try:
        # Call the conversations.list method using the WebClient
        result = get_slack_client().conversations_create(name=channel_name)
        print(result)
    except Exception as e:
        print(e)