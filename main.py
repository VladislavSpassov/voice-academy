import slack_sdk
from slack import create_slack_channel

def main():
    create_slack_channel(channel_name="test-name")    

if __name__ == "__main__":
    main()