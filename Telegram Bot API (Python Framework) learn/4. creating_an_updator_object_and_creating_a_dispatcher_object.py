# Following this Youtube video by Simplilearn: https://www.youtube.com/watch?v=227uk4kDTM8


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

# Here is a description of the 'Updator' class's attributes:
# - 'token_of_telegram_bot': This is the API token/key associated with your Telegram Bot
# - 'use_context=True': This specifies whether to use the new 'CallbackContext' based context instead of the 
#                       old 'CallbackContext' based context. Setting 'use_context=True' enables the use of the 
#                       new context, while setting 'use_context=True' enables the use of the old context. (No
#                       need know too much on this, usually you would just want to set 'use_context=True'
#                       since the new 'CallbackContext' based context is usually better when making Telegram
#                       Bots)
updater = telegram.ext.Updater(token_of_telegram_bot, use_context=True)


# Creating a 'Dispatcher' class instance/object from the class method within the 'Updator' class 
# instance/object. This 'Dispatcher' class instance/object will allow the Telegram Bot to route incoming
# updates to the appriopriate Handler class instance/objects based on the type of update received. 
# (refer to the '7. What_are_Handlers.txt' file for more about what are Handlers in the context of the
# 'telegram.ext' Telegram Bot API Python Framework)

# But you might be wondering how does 'dispatcher = updater.dispatcher', creates a 'Dispatcher' class 
# instance/object?
# By right, when you do a code like this: 'variable = [class instance].[sth here]', the '[sth here]' can only
# either be an attribute of the class (instance), or a class method. However, as seen when initiating an 
# 'Updator' class instance ('updater = telegram.ext.Updater(token_of_telegram_bot, use_context=True)'), the 
# only attributes are probably 'token' (for 'token_of_telegram_bot') and 'use_context').

# Hence, the '[sth here]' can only be class method, and here is how the 'Updator' class might look like in 
# the 'telegram.ext' Telegram Bot API Python Framework:
#       class Updater:
#           def __init__(self, token, use_context=True):
#               self.token = token
#               self.use_context = use_context

#               self.dispatcher = Dispatcher()

#       class Dispatcher:
#           /// code ///
dispatcher = updater.dispatcher

