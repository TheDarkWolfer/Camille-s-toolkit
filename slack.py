from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set up your Slack API token
slack_token = "xoxb-5596908023379-5597088559411-Yr8IFUpavuIaa9sF9ehpg0Ik"
client = WebClient(token=slack_token)

try:
    # Send a message to a channel
    response = client.chat_postMessage(
        channel="#general",
        text="Hello, Slack channel!"
    )
except SlackApiError as e:
    print(f"Error sending message: {e.response['error']}")
