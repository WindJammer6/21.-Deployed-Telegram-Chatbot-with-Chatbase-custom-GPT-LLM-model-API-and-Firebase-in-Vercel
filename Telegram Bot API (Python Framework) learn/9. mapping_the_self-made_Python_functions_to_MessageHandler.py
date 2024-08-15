# Following this Youtube video by PW Skills Tech: https://www.youtube.com/watch?v=Agkf4hEprwE&t=673s


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


# Creating the self-made Python functions that will give the Telegram Bot its functionalities. 

# Creating the 'start_python_function' self-made Python Python function's functionalities:
def start_python_function(update, context):
    update.message.reply_text("Hello, welcome to my telegram bot! (From WindJammer6)")
# This works too (see why in the '6. creating_self-made_Python_functions.py' file):
# def start_python_function(update, context):
#     update["message"].reply_text("Hello, welcome to my telegram bot! (From WindJammer6)")

# Creating the 'content_python_function' self-made Python function's functionalities
def content_python_function(update, context):
    update.message.reply_text("We have various Simplilearn (a Youtube channel) playlists available")

# Creating the 'python_python_function' self-made Python function's functionalities
def python_python_function(update, context):
    update.message.reply_text("Link of Simplilearn (a Youtube channel)'s Python tutorial playlist: https://www.youtube.com/playlist?list=PLEiEAq2VkUUJO27b6PyoSd7CJjWIPyHYO")

# Creating the 'sql_python_function' self-made Python function's functionalities
def sql_python_function(update, context):
    update.message.reply_text("Link of Simplilearn (a Youtube channel)'s SQL tutorial playlist: https://www.youtube.com/playlist?list=PLEiEAq2VkUUKL3yPbn8yWnatjUg0P0I-Z")

# Creating the 'java_python_function' self-made Python function's functionalities
def java_python_function(update, context):
    update.message.reply_text("Link of Simplilearn (a Youtube channel)'s Java tutorial playlist: https://www.youtube.com/playlist?list=PLEiEAq2VkUUI5_Z4vOtWE6AMcSrYbth1t")

# Creating the 'contact_python_function' self-made Python function's functionalities
def contact_python_function(update, context):
    update.message.reply_text("You can contact Simplilearn (a Youtube channel) on the registered mail ID provided in their website: https://www.simplilearn.com/?utm_source=bing&utm_medium=cpc&utm_term=simplilearn&utm_content=686865788-1327112179235661-&utm_device=c&utm_campaign=B-Search-Brand-APAC-ROW-AllDevice-adgroup-course-phrase&msclkid=0c8942efc9b014d3bfea24aec45ccc67")
                              
# Creating the 'help_python_function' self-made Python function's functionalities
def help_python_function(update, context):
    update.message.reply_text(
    """
    Table of contents of the available commands in this telegram bot:
    /start -> Replies with the message: "Hello, welcome to my telegram bot! (From WindJammer6)"
    /help -> This particular command
    /content -> About various PLaylists of Simplilearn (a Youtube channel)
    /python -> Directs the user to the first video of Simplilearn (a Youtube channel)'s Python tutorial playlist
    /sql -> Directs the user to the first video of Simplilearn (a Youtube channel)'s SQL tutorial playlist
    /java -> Directs the user to the first video of Simplilearn (a Youtube channel)'s Java tutorial playlist
    /contact -> Simplilearn (a Youtube channel)'s contact
    """
    )


# This is how map the self-made Python functions to the desired Handlers, and then add these mapped Handlers 
# to the 'Dispatcher' class instance/object of the Telegram Bot (which routes incoming updates (e.g. texts, 
# commands) from users/other Telegram Bots from the Telegram messaging platform server to the appropriate 
# Handler based on the type of update received). 

# Mapping the self-made Python functions to the CommandHandler (note that there are many other kinds of 
# Handlers in the 'telegram.ext' Telegram Bot API Python Framework that can handle different types of updates)
dispatcher.add_handler(telegram.ext.CommandHandler('start', start_python_function))

# Repeating this mapping process for the remaining self-made Python functions to the CommandHandler, and 
# giving a name for each command
dispatcher.add_handler(telegram.ext.CommandHandler('content', content_python_function))
dispatcher.add_handler(telegram.ext.CommandHandler('python', python_python_function))
dispatcher.add_handler(telegram.ext.CommandHandler('sql', sql_python_function))
dispatcher.add_handler(telegram.ext.CommandHandler('java', java_python_function))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact_python_function))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help_python_function))




# Creating the self-made Python functions that will give the Telegram Bot its functionalities. 

# What does the 'update.message.text' code do?
# The 'update.message.reply_text()' code is used to access the text content of an incoming message in a Telegram 
# Bot.

# Here is a breakdown of the 'update.message.reply_text()' code:
# - 'update': This is a JSON-serialized class instance/object providing access to information about the 
#             updates, such as the message text, sender, chat ID, and more.
# - 'message': This is an attribute of the 'update' class instance/object. It represents the message sent by 
#             the user. This attribute is also in turn, a 'Message' class instance/object, which also in turn 
#             contains its own attributes and methods to interact with the message, such as 
#             'message.reply_text()' (to send a text message as a reply to the message sender in the Telegram 
#             Bot), 'message.text' (to access the text of the message), 'message.sender' (to get information 
#             about the sender), and so on.
# - '.text': This is an attribute of the 'Message' class instance/object that contains the actual text of the 
#            message
def handle_message_python_function(update, context):
    update.message.reply_text(f"You said {update.message.text}")


# Mapping the self-made Python function to the MessageHandler (note that there are many other kinds of 
# Handlers in the 'telegram.ext' Telegram Bot API Python Framework that can handle different types of updates)

# MessageHandler is a Handler that handles normal text messages sent by users.

# Here is a breakdown of the code:
# - Mapping the self-made Python function, 'handle_message_python_function', to the desired Handler (which is 
#   MessageHandler in this case):
#           'telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message_python_function)'
# - Adding the mapped Handler to the 'Dispatcher' class instance/object of the Telegram Bot (which routes 
#   incoming updates (e.g. texts, commands) from users/other Telegram Bots from the Telegram messaging 
#   platform server to the appropriate Handler based on the type of update received):
#           'dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message_python_function))'
# - 'telegram.ext.Filters.text' represents the filter condition, where it filters incoming updates (e.g. texts, 
#   commands) from users/other Telegram Bots to only select those that contian text messages
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message_python_function))




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
