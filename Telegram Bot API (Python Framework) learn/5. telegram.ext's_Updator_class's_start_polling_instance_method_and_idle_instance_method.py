# Following this Youtube video by Simplilearn: https://www.youtube.com/watch?v=227uk4kDTM8 (Youtube video
# by Simplilearn, tiitled 'How To Create A Telegram Bot Using Python? | Telegram Bot In Python 
# Tutorial | Python | Simplilearn/')



# ///////////////////////////////////////////////////////////////////////////


# In this tutorial, I have already initiated a Telegram Bot in the Telegram messaging platform with the 
# following information:
# - Name: test
# - Username: test_12171_bot
# - API token/key: 6671076375:AAGIvph3qscPLo1bQmcNPrI2W9mhu4c2vv4
# - Link of this Telegram Bot: https://t.me/test_12171_bot

# The goal of this Telegram Bot is to help users navigate Simplilearn's Youtube channel. It should be able
# to help users find Simplilearn's Python, and SQL and Java playlists, as well as contain some other features.


# ///////////////////////////////////////////////////////////////////////////


# Importing 'telegram.ext', the Telegram Bot API Python Framework
import telegram.ext

# Initiating the Telegram Bot's API key/token. See how the Telegram Bot's API key/token is obtained from the
# '2. How_to_create_a_Telegram_Bot.txt' file.
token_of_telegram_bot = "6671076375:AAGIvph3qscPLo1bQmcNPrI2W9mhu4c2vv4"

# Creating an instance/object of the 'Updator' class, this 'Updator' class instance/object will allow the 
# Telegram Bot to continuously fetch updates (e.g. texts, commands) from users/other Telegram Bots from the 
# Telegram messaging platform server. 
updater = telegram.ext.Updater(token_of_telegram_bot, use_context=True)

# Creating a 'Dispatcher' class instance/object from the class method within the 'Updator' class 
# instance/object. This 'Dispatcher' class instance/object will allow the Telegram Bot to route incoming
# updates (e.g. texts, commands) from users/other Telegram Bots from the Telegram messaging platform server 
# to the appriopriate Handler class instance/objects based on the type of update received. (refer to the 
# '7. What_are_Handlers.txt' file for more about what are Handlers in the context of the 'telegram.ext' 
# Telegram Bot API Python Framework)
dispatcher = updater.dispatcher


# ///////////////////////////////////////////////////////////////////////////


# The 'start_polling()' instance method of the 'Updator' class (instance) starts an infinite loop of 
# continously checks (every few seconds) for new updates (e.g. texts, commands) from users/other Telegram Bots 
# from the Telegram messaging platform server. 

# The 'start_polling()' instance method of the 'Updator' class (instance) is also responsible for handling errors
# and displaying the errors in the IDE terminal, while continuing to poll for updates from the Telegram
# messaging platform so that the Telegram Bot remains operational and continues to fetch updates from the 
# Telegram API, even in the presence of errors.
updater.start_polling()

# The 'idle()' instance method will run after the first update (e.g. texts, commands) from users/other Telegram 
# Bots and tell the Telegram Bot to wait for further updates, rather than the 'telegram.ext' Telegram Bot API 
# Python Framework of the Telegram Bot exiting immediately after the first update.
updater.idle()

