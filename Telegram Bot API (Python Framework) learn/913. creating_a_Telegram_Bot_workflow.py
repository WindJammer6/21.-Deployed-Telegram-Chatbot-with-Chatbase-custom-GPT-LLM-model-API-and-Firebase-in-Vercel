# By ChatGPT, purpose of this file is just to test out on creating a workflow 
# in a Telegram Bot, and that the workflow can be repeated by the user.

# Laze to add comments for the individual code.


# ///////////////////////////////////////////////////////////////////////////


# I have already initiated a Telegram Bot in the Telegram messaging platform with the following information:
# - Name: test
# - Username: test_12171_bot
# - API token/key: 6671076375:AAGIvph3qscPLo1bQmcNPrI2W9mhu4c2vv4
# - Link of this Telegram Bot: https://t.me/test_12171_bot

# The goal of this Telegram Bot is serve as a improved version of the Telegram Bot that navigates 
# Simplilearn's Youtube channel. Workflow idea and code written by ChatGPT, and checked by me, that contains
# a clear workflow.

# It should be able to help users find Simplilearn's Python, and SQL and Java playlists, as well as 
# contain some other features.


# ///////////////////////////////////////////////////////////////////////////


# Workflow idea:
# 1. User Starts the Workflow
#    - User: /start
#    - Bot: "Please choose a programming language:"
#    - Options: Python, SQL, Java

# 2. User Chooses a Programming Language
#    - User: Python
#    - Bot: "You chose Python. Confirm?"
#    - Options: Show Playlist (with a button that links to the Python playlist), 
#               Restart Workflow (with a button to start over)

# 2.1. User Clicks 'Show Playlist'
#      - User: Clicks "Show Playlist"
#      - Bot: "Here is your playlist link: [youtube playlist url link]"

# 2.2. User Clicks 'Restart Workflow'
#      - User: Clicks "Restart Workflow"
#      - Bot: "Please choose a programming language:"
#      - Options: Python, SQL, Java


# ////////////////////////////////////////////////////////////////////


import telegram
import telegram.ext

def start_python_function(update, context):
    keyboard_buttons = [[telegram.KeyboardButton("Python")], [telegram.KeyboardButton("SQL")], [telegram.KeyboardButton("Java")]] 
    update.message.reply_text("Hello, welcome to my refined navigation of Simplilearn's Youtube Channel telegram bot! (From WindJammer6)\n\nPlease choose a programming language:", reply_markup=telegram.ReplyKeyboardMarkup(keyboard_buttons, one_time_keyboard=True))

def choose_playlist(update, context):
    user_choice = update.message.text

    global playlist_url

    if user_choice == "Python":
        playlist_url = "https://www.youtube.com/playlist?list=PLEiEAq2VkUUJO27b6PyoSd7CJjWIPyHYO"
    elif user_choice == "SQL":
        playlist_url = "https://www.youtube.com/playlist?list=PLEiEAq2VkUUKL3yPbn8yWnatjUg0P0I-Z"
    elif user_choice == "Java":
        playlist_url = "https://www.youtube.com/playlist?list=PLEiEAq2VkUUI5_Z4vOtWE6AMcSrYbth1t"

    inline_keyboard_buttons = [[telegram.InlineKeyboardButton("Show Playlist", callback_data="show_playlist")], [telegram.InlineKeyboardButton("Restart Workflow", callback_data="restart_workflow")]]
    update.message.reply_text(f"You chose {update.message.text}. Confirm?", reply_markup=telegram.InlineKeyboardMarkup(inline_keyboard_buttons))

def handle_callback_query_python_function(update, context):
    callback_query = update.callback_query
    update.callback_query.answer()

    if callback_query.data == 'restart_workflow':
        return start_python_function(callback_query, context)
    
    if callback_query.data == 'show_playlist':
        callback_query.edit_message_text(text=f"Here is your playlist link: {playlist_url}")


token_of_telegram_bot = "6671076375:AAGIvph3qscPLo1bQmcNPrI2W9mhu4c2vv4"
updater = telegram.ext.Updater(token_of_telegram_bot, use_context=True)
dispatcher = updater.dispatcher


dispatcher.add_handler(telegram.ext.CommandHandler('start', start_python_function))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, choose_playlist))
dispatcher.add_handler(telegram.ext.CallbackQueryHandler(handle_callback_query_python_function))


updater.start_polling()
updater.idle()