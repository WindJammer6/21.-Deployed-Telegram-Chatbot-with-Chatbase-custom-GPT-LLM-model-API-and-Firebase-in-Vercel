import os
from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
from fastapi.responses import JSONResponse

TOKEN = os.environ.get("TOKEN")
app = FastAPI()

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

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def register_handlers(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

@app.post("/webhook")
async def webhook(webhook_data: TelegramWebhook):
    try:
        bot = Bot(token=TOKEN)
        update = Update.de_json(webhook_data.dict(), bot)  # convert the Telegram Webhook class to dictionary using .dict() method
        dispatcher = Dispatcher(bot, None, workers=4)
        register_handlers(dispatcher)
        dispatcher.process_update(update)
        return {"message": "ok"}
    except Exception as e:
        logging.error(f"Error processing webhook: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

@app.get("/")
def index():
    return {"message": "Hello World"}
