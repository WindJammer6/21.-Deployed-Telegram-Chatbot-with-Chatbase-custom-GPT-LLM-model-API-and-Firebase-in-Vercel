# This file works for the Telegram Chatbot with the initially used PyMySQL server's database, rather than the Firebase's Realtime database

import os
import json
import requests
from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import pymysql

# Configuration for Chatbase, Telegram Bot and PyMySQL
# MYSQL_SERVER_HOST = os.environ.get('MYSQL_SERVER_HOST')
# MYSQL_SERVER_USER = os.environ.get('MYSQL_SERVER_USER')
# MYSQL_SERVER_PASSWORD = os.environ.get('MYSQL_SERVER_PASSWORD')
# MYSQL_SERVER_DATABASE = os.environ.get('MYSQL_SERVER_DATABASE')
CHATBASE_API_URL = 'https://www.chatbase.co/api/v1/chat'
CHATBASE_API_KEY = os.environ.get('CHATBASE_API_KEY')
CHATBASE_CHATBOT_ID = os.environ.get('CHATBASE_CHATBOT_ID')
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')  # Make sure to set this in your environment variables

# FastAPI app instance
app = FastAPI()

# Headers for Chatbase API requests
headers = {
    'Authorization': f'Bearer {CHATBASE_API_KEY}',
    'Content-Type': 'application/json'
}

# Data structure for conversation history
conversation_history = {
    "messages": [],
    "chatbotId": CHATBASE_CHATBOT_ID,
    "stream": False,
    "temperature": 0
}

# Setting up the MySQL server:
# my_sql_relational_database_connection = pymysql.connect(
#     host=os.getenv("MYSQL_SERVER_HOST"),
#     user=os.getenv("MYSQL_SERVER_USER"),
#     password=os.getenv("MYSQL_SERVER_PASSWORD"),
#     database=os.getenv("MYSQL_SERVER_DATABASE")
# )

# cursor = my_sql_relational_database_connection.cursor()

# Pydantic model for validating Telegram webhook data
class TelegramWebhook(BaseModel):
    update_id: int
    message: Optional[dict]
    edited_message: Optional[dict]
    channel_post: Optional[dict]
    edited_channel_post: Optional[dict]
    inline_query: Optional[dict]
    chosen_inline_result: Optional[dict]
    callback_query: Optional[dict]
    shipping_query: Optional[dict]
    pre_checkout_query: Optional[dict]
    poll: Optional[dict]
    poll_answer: Optional[dict]

# Ensure that TELEGRAM_TOKEN is correctly retrieved
if TELEGRAM_TOKEN is None:
    raise ValueError("TELEGRAM_TOKEN environment variable is not set.")

# Create a Telegram bot instance
bot = Bot(token=TELEGRAM_TOKEN)  # Use the environment variable

# Initialize the dispatcher
dispatcher = Dispatcher(bot, None, workers=4)

# Command handler for /start command
def start(update, context):
    update.message.reply_text("Hello, welcome to my telegram bot integrated with Chatbase custom GPT model API! (From Goh Jet Wei (WindJammer6))")

# Command handler for /help command
def help_command(update, context):
    update.message.reply_text(
        """
        Table of contents of the available commands in this telegram bot:
        /start -> Replies with the message: "Hello, welcome to my telegram bot integrated with Chatbase custom GPT model API! (From Goh Jet Wei (WindJammer6))"
        /help -> This help message
        
        Type anything else to get a response from the Chatbase custom GPT model!
        """
    )

# Handler for processing incoming messages
def handle_message(update, context):
    user_message = update.message.text
    conversation_history["messages"].append({"content": user_message, "role": "user"})

    # Make API call to Chatbase
    response = requests.post(CHATBASE_API_URL, headers=headers, data=json.dumps(conversation_history))
    json_data = response.json()

    if response.status_code == 200:
        chatbase_response = json_data['text']
        update.message.reply_text(f"Chatbase custom GPT model: {chatbase_response}")
        conversation_history["messages"].append({"content": chatbase_response, "role": "assistant"})

        
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////


        # # Telegram Chatbot to MySQL server's Relational Database's table things

        # # Inserting the student's prompt and telegram chatbot's response as a row in the MySQL server's Relational Database's 
        # # table using parameterized query.
        # telegram_chatbot_response = json_data['text']
        # query = "INSERT INTO telegram_chatbot_history (student_prompt, telegram_chatbot_response) VALUES (%s, %s)"
        # cursor.execute(query, (update.message.text, telegram_chatbot_response))

        # # Commit the transaction (idk why but this is just needed here to prevent errors)
        # my_sql_relational_database_connection.commit()


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

    
    else:
        update.message.reply_text(f"Error: {json_data.get('message', 'An error occurred')}")

# Register handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

@app.post("/webhook")
async def webhook(request: Request):
    # Parse the incoming update
    webhook_data = await request.json()
    update = Update.de_json(webhook_data, bot)
    dispatcher.process_update(update)
    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}


