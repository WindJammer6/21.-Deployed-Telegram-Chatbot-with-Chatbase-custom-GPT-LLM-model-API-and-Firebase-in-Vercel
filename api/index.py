import os
import json
import requests
from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# Configuration for Chatbase and Telegram Bot
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
    update.message.reply_text("Hello, welcome to my telegram bot integrated with Chatbase custom GPT model API!")

# Command handler for /help command
def help_command(update, context):
    update.message.reply_text(
        """
        Table of contents of the available commands in this telegram bot:
        /start -> Replies with a welcome message
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


