# The initiated Telegram Bot in this file in the Telegram messaging platform has the following information:
# - Name: Telegram_Chatbot_integrated_with_Chatbase_GPT_model_API_test
# - Username: test_12173_bot
# - API token/key: 7045977515:AAGGa78vjXmfTDzMPoCAkm2NsGpiYOi5WzI
# - Link of this Telegram Bot: https://t.me/test_12173_bot

# The goal of this Telegram Bot is to test the integration of the Chatbase custom GPT model API (Large
# Language Model (LLM) to a Telegram Bot.

# Chatbase custom GPT model API documentation: https://docs.chatbase.co/docs/create-a-chatbot 


# ///////////////////////////////////////////////////////////////////////////


# Instructions to integrating your own trained Chatbase custom GPT model API to this Telegram Bot code:
# Simply replace your Chatbase custom GPT model API key (e.g. 3c255g98b-c5fe-4324a7-343eb-f5d4353536e (this is a
# fake API key)) with the '<API KEY HERE>'! If you are not sure how to find your Chatbase custom GPT model API 
# key, see the instructions below under the section, 'How to find the Chatbase custom GPT model API key'

# Also replace your Chatbase custom GPT model chatbot ID (e.g. -f0oTRCOFh5frn2dPpi (this is a
# fake API key)) with the '<CHATBOT ID HERE>'! If you are not sure how to find your Chatbase custom GPT model chatbot 
# ID, see the instructions below under the section, 'How to find the Chatbase custom GPT model chatbase ID'


# ///////////////////////////////////////////////////////////////////////////


import requests
import json
import telegram
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from flask import Flask, request, jsonify
import telegram.ext     # (Note that the version of the telegram Python library is version 13.3)


# Initialize Flask app for webhook
app = Flask(__name__)


# Chatbase custom GPT model API, but with Python's 'requests' and json' libraries as substitude, because
# Chatbase custom GPT model API does not have their own Python library code unlike OpenAI GPT model API 
url = 'https://www.chatbase.co/api/v1/chat'


# How to find the Chatbase custom GPT model API key:
# 1. Log in to Chatbase: Go to the Chatbase website and log in with your Google account credentials.
# 2. Navigate to Your Account: After logging in, navigate to the dashboard where you can manage your 
#    chatbots, settings and view analytics.
# 3. Access API Settings: In your Chatbase dashboard, look for settings options under the "Settings" 
#    menu.
# 4. Find Your API Key: Within the developer or API settings, you should find your API key, labeled as 
#    "API Key".
headers = {
    'Authorization': 'Bearer 3c7b798b-c5fe-41a7-bdeb-f5d0b6f8536e',
    'Content-Type': 'application/json'
}

# How to find the Chatbase custom GPT model chatbot ID:
# 1. Log in to Chatbase: Go to the Chatbase website and log in with your Google account credentials.
# 2. Navigate to the Dashboard:After logging in, navigate to the dashboard where you can manage your 
#    chatbots, settings and view analytics.
# 3. Select Your chatbot: From the dashboard, locate the chatbot for which you want to find the chatbot ID. 
#    You might see a list of chatbots if you have more than one. Click on the chatbot's name or the 
#    associated link to access its details.
# 4. Access chatbot Settings: After selecting your bot, look for a "Settings" option. This is usually found 
#    in the sidebar or in the top menu.
# 5. Find the Bot ID: Within the settings, you should see various details about your bot, including its name, 
#    platform, and other configurations. Look for a section labeled "Bot ID" or "API Key." This is your 
#    chatbot's unique identifier in Chatbase.
# 6. Copy the Bot ID: Once you find the Bot ID, you can copy it for use in your applications or integrations.
conversation_history_and_other_data = {
    "messages": [],
    "chatbotId": "wGS8ehg-39TolweihWY3w",
    "stream": False,
    "temperature": 0
}

# With reference from code in the Chatbase custom GPT model API documentation:
    # conversation_history_and_other_data = {
    #     "messages": [
    #         {"content": "How can I help you?", "role": "assistant"},
    #         {"content": "What is chatbase?", "role": "user"}
    #     ],
    #     "chatbotId": "<Your Chatbot ID>",
    #     "stream": False,
    #     "temperature": 0
    # }


#  //////////////////////////////////////////////////////////////////////////////////////////


# Telegram Bot code with the 'telegram.ext' Telegram Bot API Python Framework 

# This Telegram Bot has 2 commands:
# - /start: prints out a welcome message to the user to the Telegram Bot
# - /help: prints out a directory of the available commands
token_of_telegram_bot = "7045977515:AAGGa78vjXmfTDzMPoCAkm2NsGpiYOi5WzI"

# Set up dispatcher to handle incoming messages
bot = telegram.Bot(token=token_of_telegram_bot)
dispatcher = Dispatcher(bot, None, use_context=True)

def start_python_function(update, context):
    update.message.reply_text("Hello, welcome to my telegram bot integrated with Chatbase custom GPT model API! (From Goh Jet Wei (WindJammer6))")

def help_python_function(update, context):
    update.message.reply_text(
    """
    Table of contents of the available commands in this telegram bot:
    /start -> Replies with the message: "Hello, welcome to my telegram bot integrated with Chatbase custom GPT model API! (From Goh Jet Wei (WindJammer6))"
    /help -> This particular command

    Type anything else to get a response from the Chatbase custom GPT model!
    """
    )



# /////////////////////////////////////////////////////////////////////////////////////////


# The most important function that blends both the Chatbase custom GPT model API and the 'telegram.ext' 
# Telegram Bot API Python Framework 
def handle_message_python_function(update, context):

    # Appending the user message/prompt to the 'conversation_history_and_other_data' before making the API call
    conversation_history_and_other_data["messages"].append({"content": update.message.text, "role": "user"})


    # Generating the Chatbase custom GPT response to the user message/prompt when making the API call
    response = requests.post(url, headers=headers, data=json.dumps(conversation_history_and_other_data))
    json_data = response.json()

    # If there is no error generating the Chatbase custom GPT response
    if response.status_code == 200:
        update.message.reply_text(f"Chatbase custom GPT model: {json_data['text']}")
        # Appending the generated Chatbase custom GPT response to the 'conversation_history_and_other_data' 
        conversation_history_and_other_data["messages"].append({"content": json_data['text'], "role": "assistant"})

    # If there is an error when generating the Chatbase custom GPT response for some reason
    else:
        print(f"Error: {json_data}")
        update.message.reply_text(f"Chatbase custom GPT model: Oh no! You encountered an error in the code! The error is: \n'{json_data['message']}'")

    # With reference from code in the Chatbase custom GPT model API documentation:
    #     if response.status_code == 200:
    #         print("response:", json_data['text'])
    #     else:
    #         print('Error:' + json_data['message'])


# //////////////////////////////////////////////////////////////////////////////////////////


# More Telegram Bot code with the 'telegram.ext' Telegram Bot API Python Framework 
dispatcher.add_handler(CommandHandler('start', start_python_function))
dispatcher.add_handler(CommandHandler('help', help_python_function))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message_python_function))


# //////////////////////////////////////////////////////////////////////////////////////////


# Webhook Functions:
# Set up your webhook endpoint that Telegram will use to send messages to your bot.
@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming message as a Telegram update
    update = telegram.Update.de_json(request.get_json(), bot)
    dispatcher.process_update(update)
    return "ok", 200


# //////////////////////////////////////////////////////////////////////////////////////////


# Run the Flask App
if __name__ == "__main__":
    app.run(port=5000)
