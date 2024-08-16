from typing import Dict, Optional
from pydantic import BaseModel
from fastapi import FastAPI, Request
import requests
import os
import json
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import firebase_admin
from firebase_admin import db

# Configuration for Chatbase, Telegram Bot, and Firebase
FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL')
CHATBASE_API_URL = 'https://www.chatbase.co/api/v1/chat'
CHATBASE_API_KEY = os.environ.get('CHATBASE_API_KEY')
CHATBASE_CHATBOT_ID = os.environ.get('CHATBASE_CHATBOT_ID')
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

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

# Setting up Firebase
if not firebase_admin._apps:
    credentials_object = firebase_admin.credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(credentials_object, {
        'databaseURL': FIREBASE_DATABASE_URL
    })

# Define Pydantic model for validating Telegram webhook data
class Message(BaseModel):
    message_id: int
    from_user: Optional[Dict[str, str]] = None
    chat: Dict[str, str]
    date: int
    text: Optional[str] = None

class TelegramWebhook(BaseModel):
    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None
    inline_query: Optional[Dict[str, str]] = None
    chosen_inline_result: Optional[Dict[str, str]] = None
    callback_query: Optional[Dict[str, str]] = None
    shipping_query: Optional[Dict[str, str]] = None
    pre_checkout_query: Optional[Dict[str, str]] = None
    poll: Optional[Dict[str, str]] = None
    poll_answer: Optional[Dict[str, str]] = None

# Get a reference to the Firebase database
reference_to_database = db.reference('/')

# Read data from the Realtime Database from Firebase
print(reference_to_database.get())

# Ensure TELEGRAM_TOKEN is correctly retrieved
if TELEGRAM_TOKEN is None:
    raise ValueError("TELEGRAM_TOKEN environment variable is not set.")

# Create a Telegram bot instance
bot = Bot(token=TELEGRAM_TOKEN)

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

    # Make API call to Ch

