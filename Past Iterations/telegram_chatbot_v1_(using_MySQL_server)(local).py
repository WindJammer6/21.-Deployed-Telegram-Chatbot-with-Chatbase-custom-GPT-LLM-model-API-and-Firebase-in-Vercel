# The initiated Telegram Bot in this file in the Telegram messaging platform has the following information:
# - Name: Telegram_Chatbot_integrated_with_Chatbase_GPT_model_API_test
# - Username: test_12173_bot
# - API token/key: 7045977515:AAGGa78vjXmfTDzMPoCAkm2NsGpiYOi5WzI
# - Link of this Telegram Bot: https://t.me/test_12173_bot

# The goal of this Telegram Bot is to test the integration of the Chatbase custom GPT model API (Large
# Language Model (LLM) to a Telegram Bot.

# Chatbase custom GPT model API documentation: https://docs.chatbase.co/docs/create-a-chatbot 

import requests
import json
import telegram.ext     # (Note that the version of the telegram Python library is version 13.3)
import pymysql

url = 'https://www.chatbase.co/api/v1/chat'

headers = {
    'Authorization': 'Bearer 3c7b798b-c5fe-41a7-bdeb-f5d0b6f8536e',
    'Content-Type': 'application/json'
}

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
    

# //////////////////////////////////////////////////////////////////////////////////////////


# Setting up the MySQL server:
my_sql_relational_database_connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="urop_telegram_chatbot_db"
)

cursor = my_sql_relational_database_connection.cursor()


# //////////////////////////////////////////////////////////////////////////////////////////


# Telegram Bot code with the 'telegram.ext' Telegram Bot API Python Framework 

# This Telegram Bot has 2 commands:
# - /start: prints out a welcome message to the user to the Telegram Bot
# - /help: prints out a directory of the available commands
token_of_telegram_bot = "7045977515:AAGGa78vjXmfTDzMPoCAkm2NsGpiYOi5WzI"

updater = telegram.ext.Updater(token_of_telegram_bot, use_context=True)

dispatcher = updater.dispatcher

def start_python_function(update, context):
    update.message.reply_text("Hello, welcome to my telegram chatbot integrated with Chatbase custom GPT model API! (From Goh Jet Wei (WindJammer6))")

def help_python_function(update, context):
    update.message.reply_text(
    """
    Table of contents of the available commands in this telegram bot:
    /start -> Replies with the message: "Hello, welcome to my telegram chatbot integrated with Chatbase custom GPT model API! (From Goh Jet Wei (WindJammer6))"
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
        print(conversation_history_and_other_data["messages"])


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////


        # Telegram Chatbot to MySQL server's Relational Database's table things

        # Inserting the student's prompt and telegram chatbot's response as a row in the MySQL server's Relational Database's 
        # table using parameterized query.
        telegram_chatbot_response = json_data['text']
        query = "INSERT INTO telegram_chatbot_history (student_prompt, telegram_chatbot_response) VALUES (%s, %s)"
        cursor.execute(query, (update.message.text, telegram_chatbot_response))

        # Commit the transaction (idk why but this is just needed here to prevent errors)
        my_sql_relational_database_connection.commit()


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////
        

    # If there is an error when generating the Chatbase custom GPT response for some reason
    else:
        print(f"Error: {json_data}")
        update.message.reply_text(f"Chatbase custom GPT model: Oh no! You encountered an error in the code! The error is: \n'{json_data['message']}'")


# //////////////////////////////////////////////////////////////////////////////////////////


# More Telegram Bot code with the 'telegram.ext' Telegram Bot API Python Framework 
dispatcher.add_handler(telegram.ext.CommandHandler('start', start_python_function))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help_python_function))

dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message_python_function))

updater.start_polling()
updater.idle()
