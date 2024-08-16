import os
import json
import requests
from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from firebase_admin import db
import firebase_admin

# Configuration for Chatbase, Telegram Bot and Firebase
FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL')
CHATBASE_API_URL = 'https://www.chatbase.co/api/v1/chat'
CHATBASE_API_KEY = os.environ.get('CHATBASE_API_KEY')
	@@ -41,31 +41,34 @@
        'databaseURL': FIREBASE_DATABASE_URL
    })

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


# Get a reference to the Firebase database
reference_to_database = db.reference('/')

# Read data from the Realtime Database from Firebase
print(reference_to_database.get())


# Ensure that TELEGRAM_TOKEN is correctly retrieved
if TELEGRAM_TOKEN is None:
    raise ValueError("TELEGRAM_TOKEN environment variable is not set.")
	@@ -106,20 +109,11 @@ def handle_message(update, context):
        update.message.reply_text(f"Chatbase custom GPT model: {chatbase_response}")
        conversation_history["messages"].append({"content": chatbase_response, "role": "assistant"})


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////


        # Telegram Chatbot to Firebase's Realtime Database things

        #If confirmation submit button is pressed in the Streamlit (Python) web application, the program will 'push' 
        #basically add this new pieces of user data into the Realtime database in Firebase    
        reference_to_database.push({"student_prompt" : update.message.text, "telegram_chatbot_response" : json_data['text']})    


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    else:
        update.message.reply_text(f"Error: {json_data.get('message', 'An error occurred')}")

	@@ -139,3 +133,4 @@ async def webhook(request: Request):
@app.get("/")
def index():
    return {"message": "Hello World"}
