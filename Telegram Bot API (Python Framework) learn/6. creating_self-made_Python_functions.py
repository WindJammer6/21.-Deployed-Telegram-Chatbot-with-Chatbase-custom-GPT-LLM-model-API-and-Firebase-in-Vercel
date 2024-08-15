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
updater = telegram.ext.Updater(token_of_telegram_bot, use_context=True)

# Creating a 'Dispatcher' class instance/object from the class method within the 'Updator' class 
# instance/object. This 'Dispatcher' class instance/object will allow the Telegram Bot to route incoming
# updates (e.g. texts, commands) from users/other Telegram Bots from the Telegram messaging platform server 
# to the appriopriate Handler class instance/objects based on the type of update received. (refer to the 
# '7. What_are_Handlers.txt' file for more about what are Handlers in the context of the 'telegram.ext' 
# Telegram Bot API Python Framework)
dispatcher = updater.dispatcher




# Creating the self-made Python functions that will give the Telegram Bot its functionalities. There self-made
# Python functions can only have 2 parameters. Though the 2 parameters of the self-made Python functions can 
# be named as anything, it is convention, for the 'telegram.ext' Telegram Bot API Python Framework, to name
# the first parameter 'update', and the second parameter 'context'. 

# Here is a description of the each of the 2 parameters:
# - 'update': This parameter represents an incoming update (e.g. texts, commands) from users/other Telegram 
#             Bots from the Telegram messaging platform server. 'update' is a JSON-serialized class 
#             instance/object providing access to information about the updates, such as the message text, 
#             sender, chat ID, and more.
# - 'context': This parameter provides additional contextual information and functionality to the Handler.
#              It is a class instance/object that contains various attributes and methods to interact with the 
#              Telegram Bot's environment and Telegram API. For example, it provides methods to send messages, 
#              access user data, manage conversation states, and more. (refer to the '7. What_are_Handlers.txt'
#              file for more about what are Handlers in the context of the 'telegram.ext' Telegram Bot API 
#              Python Framework)

#              (However, the 'context' parameter is rarely used in simpler Telegram Bot implementations)

# Note that the names for these self-made Python functions are not the direct commands for the Telegram Bot!
# You need to make use of the different Handlers in the 'telegram.ext' Telegram Bot API Python Framework and 
# map these self-made Python functions to the desired Handlers, and then add these mapped Handlers to the 
# 'Dispatcher' class instance/object of the Telegram Bot (which routes incoming updates (e.g. texts, commands) 
# from users/other Telegram Bots from the Telegram messaging platform server to the appropriate Handler based 
# on the type of update received). 

# You can think of it as these self-made Python functions being the code that define the functionality/behaviour
# of the Handlers in the 'telegram.ext' Telegram Bot API Python Framework (refer to the 
# '7. What_are_Handlers.txt' file for more about what are Handlers in the context of the 'telegram.ext' 
# Telegram Bot API Python Framework).

# Refer to the '8. mapping_the_self-made_Python_functions_to_Handlers.py' file to see how the mapping of the
# self-made Python functions to the desired Handlers, and how then these mapped Handlers are added to the 
# 'Dispatcher' class instance/object of the Telegram Bot 



# What does the 'update.message.reply_text()' code do?
# The 'update.message.reply_text()' code is used to send a text message as a reply to the message sender.

# Here is a breakdown of the 'update.message.reply_text()' code:
# - 'update': This is a JSON-serialized object (basically a Python dictionary) providing access to information 
#             about the updates, such as the message text, sender, chat ID, and more.
# - 'message': This is a key of the 'update' JSON-serialized object/Python dictionary. It's value represents 
#              a 'Message' class instance/object containing the message by the user, which also in turn 
#              contains its own attributes and methods to interact with the 'Message' class instance/object, 
#              such as 'message.reply_text()' (to send a text message as a reply to the message sender in the 
#              Telegram Bot), 'message.text' (to access the text of the message), 'message.sender' (to get 
#              information about the sender), and so on.
#              (Note: Here is how a JSON-serialized object (basically a Python dictionary) looks like in 
#                     Python:
#                      ```
                       # import json

                       # # Sample Python dictionary
                       # update = {
                       #     "message": Message(),
                       #     "chat-id": 23435465730,
                       # }

                       # # Serialize the Python dictionary to JSON
                       # json_string = json.dumps(update)

                       # print(json_string)`
#                      ```
#               )      
                      
# - 'reply_text()': This is an instance method in the 'Message' class instance/object that will send a text 
#                   message as a reply to the message sender in the Telegram Bot.

# Creating the 'start_python_function' self-made Python Python function's functionalities:
def start_python_function(update, context):
    update.message.reply_text("Hello, welcome to my telegram bot! (From WindJammer6)")
# This works too:
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

