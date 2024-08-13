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
dispatcher = Dispat

