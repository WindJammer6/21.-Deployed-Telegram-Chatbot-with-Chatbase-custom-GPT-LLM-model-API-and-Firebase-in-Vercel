# Following this Youtube video by Code with Ibrahim: https://www.youtube.com/watch?v=Agkf4hEprwE&t=673s
# (Youtube video by Code with Ibrahim, titled 'Python Telegram Bot with Custom Keyboard, Buttons, and 
# Images')


# ///////////////////////////////////////////////////////////////////////////


# In this tutorial, I have already initiated a Telegram Bot in the Telegram messaging platform with the 
# following information:
# - Name: test2
# - Username: test_12174_bot
# - API token/key: 7291429066:AAH5o8JUQbd8Ieh7utHtbBFWJNf1oriEXdA
# - Link of this Telegram Bot: https://t.me/test_12174_bot

# The goal of this Telegram Bot is to display images of a random person's face or a random thing, depending 
# on which keyboard button, 'Random Person's Face' or 'Random Thing' is pressed.

# Then, users can choose to 'Like' or 'Dislike' the image, depending on which inline keyboard button,
# '👍' or '👎' is pressed.


# ///////////////////////////////////////////////////////////////////////////


# Prerequisites of creating this Telegram Bot:
# We will also be using the 'requests' Python library to retrieve information from 2 different websites.
# Namely, information that is:
# - the image of a random person's face from the following website: https://thispersondoesnotexist.com/
# - the image of a random thing from the following website: https://picsum.photos/200

# (Note: These are some pretty interesting websites... when you rerun the link in the searh bar, you
#  will just get different random person's images (for the https://thispersondoesnotexist.com/ website) 
#  and random thing images (for the https://picsum.photos/200 website) respectively)


# ///////////////////////////////////////////////////////////////////////////


# Importing 'telegram.ext', the Telegram Bot API Python Framework
import telegram.ext

# Importing 'telegram', another Telegram Bot API Python Framework to use the 'telegram.KeyboardButton()'
# class and 'telegram.ReplyKeyboardMarkup' class to create the keyboard buttons (see below)
import telegram

# Importing 'requests' Python library
import requests


# Initiating the Telegram Bot's API key/token. See how the Telegram Bot's API key/token is obtained from the
# '2. How_to_create_a_Telegram_Bot.txt' file.
token_of_telegram_bot = "7291429066:AAH5o8JUQbd8Ieh7utHtbBFWJNf1oriEXdA"

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


# Creating the self-made Python functions that will give the Telegram Bot its functionalities. 
# Creating the 'start_python_function' self-made Python Python function's functionalities:
def start_python_function(update, context):

    # Creating the keyboard buttons using the telegram (Python) library's 'KeyboardButton' class
    keyboard_buttons = [[telegram.KeyboardButton("Random Person's Face")], [telegram.KeyboardButton("Random Thing")]] 
    
    # Creating the custom reply keyboard using the telegram (Python) library's 'ReplyKeyboardMarkup' class,
    update.message.reply_text("Hello, welcome to my random image posts telegram bot! (From WindJammer6)", reply_markup=telegram.ReplyKeyboardMarkup(keyboard_buttons))


# Mapping the self-made Python functions to the CommandHandler (note that there are many other kinds of 
# Handlers in the 'telegram.ext' Telegram Bot API Python Framework that can handle different types of updates)

# CommandHandler is a Handler that Handles commands sent by users.
dispatcher.add_handler(telegram.ext.CommandHandler('start', start_python_function))


# ///////////////////////////////////////////////////////////////////////////


# Creating the self-made Python functions that will give the Telegram Bot its functionalities. 
def handle_message_python_function(update, context):

    # Telling the Telegram Bot to send an image of a random person's face using the website link, 
    # 'https://thispersondoesnotexist.com/', whenever the reply message "Random Person's Face" is 
    # sent by the user.
    if update.message.text == "Random Person's Face":
        
        # What does the 'requests.get().content' code do?
        # The 'requests.get().content' code is uses the 'requests' Python library to fetch content from a 
        # website. 
        
        # Here is a breakdown of the 'requests.get().content' code:
        # - 'requests' - initiating the 'requests' Python library
        # - 'get()'    - this is a function in the 'requests' Python library that sends an HTTP GET request
        #                to a website. You can specify the website by specifying the URL of the website as
        #                a parameter input in this function. It returns a 'Response' class instance/object,
        #                contains many attributes, with some of the common ones being:
        #                -> 'status_code' - The HTTP status code of the response (e.g., 200 for success, 
        #                                   404 for not found).
        #                -> 'content'     - The raw binary content of the response (useful for non-text 
        #                                   data like images or files).
        #                -> 'text'        - The textual content of the response, decoded as a string (useful 
        #                                   for text responses like HTML or JSON).
        # - 'content'  - (an attribute of the 'Response' class instance/object returned by the 'get()' 
        #                 'requests' Python library function) (see above)
        image = requests.get('https://thispersondoesnotexist.com/').content
    

    # Telling the Telegram Bot to send an image of a random image using the website link, 
    # 'https://picsum.photos/200', whenever the reply message "Random Thing" is sent by the user.
    if update.message.text == "Random Thing":
        # /// see comments of this line of code above ///
        image = requests.get('https://picsum.photos/200').content


    # If an image is retrieved from either the 'https://thispersondoesnotexist.com/' or 
    # 'https://picsum.photos/200' website, send the image reply
    if image:
        
        # What does the 'update.message.reply_media_group()' code do?
        # The 'update.message.reply_media_group()' code is used to send media files (e.g. image, 
        # videos, soundtrack, etc.) as a reply to the message sender.

        # Here is a breakdown of the 'update.message.reply_media_group()' code:
        # - 'update' : (refer to the '6. creating_self-made_Python_functions.py' file)
        # - 'message': (refer to the '6. creating_self-made_Python_functions.py' file)
        # - 'reply_text()': This is an instance method in the 'Message' class instance/object that will send media files 
        #                   (e.g. image, videos, soundtrack, etc.) as a reply to the message sender in the Telegram Bot. 
        #                   It takes in many parameters, but 2 of the most common ones are:
        #                   -> 'media'        - the media files (e.g. image, videos, soundtrack, etc.) to send
        #                   -> 'reply_markup' - adds interactive elements such as inline keyboard buttons and keyboard
        #                                       buttons that you can use instead to send a text reply to the meesage
        #                                       (you can see how this is done in the '910. telegram's_KeyboardButton_
        #                                       class_and_ReplyKeyboardMarkup_class.py' file)

        # What does the 'telegram.InputMediaPhoto' class do?
        # It represents a photo to be sent. It takes in many parameters, but 2 of the most common ones are:
        # -> 'image'   - represents the photo to be sent. It can be a file ID of a previously uploaded photo, an URL 
        #                pointing to the photo, or a file object (such as an image file) 
        # -> 'caption' - represents the caption for the photo. Takes in a string datatype
        update.message.reply_media_group(media=[telegram.InputMediaPhoto(image, caption="This is the caption of this random person's face image.")])
        # This works too:
        # context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[telegram.InputMediaPhoto(image, caption="This is the caption of this random person's face image.")])

        # Here is a breakdown of the 'context.bot.sendMediaGroup()' code:
        # - 'context': (refer to the '910. telegram's_KeyboardButton_class_and_ReplyKeyboardMarkup_class.py' file)
        # - 'bot'    : (refer to the '910. telegram's_KeyboardButton_class_and_ReplyKeyboardMarkup_class.py' file)                      
        # - 'sendMediaGroup()': This is an instance method in the Telegram Bot class instance/object that will send a text 
        #                       reply message as a reply to the message sender in a specific chat in the Telegram Bot, which
        #                       you can specify using the 'chat_id' parameter (see below). It takes in many parameters, but 
        #                       3 of the most common ones are:
        #                       -> 'chat_id'      - represents the specific chat in the Telegram Bot to send a text reply
        #                                           message as a reply to the message sender. You can retrieve identification 
        #                                           information of the specific chat in the Telegram Bot using the code:
        #                                           'update.effective_chat.id' by letting this code be the input of this
        #                                           parameter
        #                       -> 'media'        - the media files (e.g. image, videos, soundtrack, etc.) to send
        #                       -> 'reply_markup' - adds interactive elements such as inline keyboard buttons and keyboard
        #                                           buttons that you can use instead to send a text reply to the meesage
        #                                           (you can see how this is done in the '910. telegram's_KeyboardButton_
        #                                           class_and_ReplyKeyboardMarkup_class.py' file)


        # How is the 'context.bot.send_message()' code different from the 'update.message.reply_text()' code?
        # Both does the same thing which is both are used to send messages to users in Telegram Bot interactions

        # The only difference is that the 'context.bot.send_message()' code offers an additional functionality by allowing
        # you to specify which chat in the Telegram Bot to send the message to, while the 'update.message.reply_text()' code
        # is shorter, and is just programmed to just send the message to the same chat of the conversation in the Telegram Bot.



        # To create inline keyboard buttons such as '👍' or '👎' in the telegram bot, in the telegram
        # bot inline keyboard, you will need to use the telegram (Python) library's 'InlineKeyboardButton' 
        # class and 'InlineKeyboardMarkup' class, and here is what each of them do respectively:
        # - 'InlineKeyboardButton' class - represents a single button in an inline keyboard.
        #                                  Unlike the 'KeyboardButton' class's button, this button does not 
        #                                  send a predefined reply to the Telegram Bot, but rather triggers 
        #                                  a callback query or opens a URL when pressed. 
        # - 'InlineKeyboardMarkup' class - used to display a custom inline keyboard directly attached to 
        #                                  the message. Unlike the 'ReplyKeyboardMarkup' class's custom reply
        #                                  keyboard, this keyboard does not replace the default keyboard, but 
        #                                  ratherd, it is embedded within the message and is designed to 
        #                                  interact with the Telegram Bot without sending new messages.

        # Creating the keyboard buttons using the telegram (Python) library's 'InlineKeyboardButton' class 
        inline_keyboard_buttons = [[telegram.InlineKeyboardButton("👍", callback_data="like")], [telegram.InlineKeyboardButton("👎", callback_data="dislike")]]
        

        # Creating the custom reply keyboard using the telegram (Python) library's 'InlineKeyboardMarkup' class,
        # and putting it as an input of the 'reply_markup' parameter of the 'reply_text()' instance method
        # in the 'Message' class instance/object

        # (Note: There is an additional 'reply_markup' parameter being used in the 'reply_text()' instance method 
        #  in the 'Message' class instance/object here. See what it does in the '6. creating_self-made_Python_
        #  functions.py' file)
        update.message.reply_text("Did you like the image?", reply_markup=telegram.InlineKeyboardMarkup(inline_keyboard_buttons))
        # This works too:
        # context.bot.send_message(chat_id=update.effective_chat.id, text="Did you like the image?", reply_markup=telegram.InlineKeyboardMarkup(inline_keyboard_buttons))



# Mapping the self-made Python function to the MessageHandler (note that there are many other kinds of 
# Handlers in the 'telegram.ext' Telegram Bot API Python Framework that can handle different types of updates)

# MessageHandler is a Handler that handles normal text messages sent by users.
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message_python_function))


# ///////////////////////////////////////////////////////////////////////////


# However, the Inline Keyboard is different from the Reply Keyboard, and triggers a special type of update
# known as a callback query, rather than a reply message, and callback queries will need to be handled 
# differently from a regular reply message. If you ran the code without this section/handling the 
# callback queries, if the inline keyboard buttons are clicked, there will be a 'timer' that will 
# continuously run on the Inline Keyboard buttons, indicating that the trigeered callback query is
# waiting to be handled, but will never be, so the 'timer' will run infinitely.

# What is a Callback Query?
# A callback query is a special type of update triggered when a user presses a button from an inline keyboard
# in a Telegram Bot.

# We will handle the callback query by introducing a 'Like' and 'Dislike' counter, which will be incremented
# whenever the Inline Keyboard button "👍" and Inline Keyboard button "👎" is clicked, and the updated 
# counter will be printed in the terminal (not the Telegram Bot!)


# Creating the self-made Python functions that will give the Telegram Bot its functionalities. 

# 'Likes' and 'Dislikes' counter defined as global variables
likes = 0
dislikes = 0

def handle_callback_query_python_function(update, context):

    # What does the 'update.callback_query.data' code do?
    # The 'update.callback_query.data' code is used to retrieve the data stored in a callback query

    # Here is a breakdown of the 'update.callback_query.data' code:
    # - 'update': This is a JSON-serialized class instance/object providing access to information about the 
    #             updates, such as the message text, sender, chat ID, and more.
    # - 'callback_query': This is an attribute of the 'update' class instance/object. It represents the callback query
    #                     triggered by an action done by the user (i.e. the clicking of a inline keyboard button). This 
    #                     attribute is also in turn, a 'CallbackQuery' class instance/object, which also in turn 
    #                     contains its own attributes and methods to interact with the message, with some of the most
    #                     common ones are: 
    #                     -> 'callback_query.answer()': Acknowledge the callback query. This method sends a notification to the 
    #                                                   user that their action was received.
    #                     -> 'callback_query.data'    : to access the data associated with the callback query
    #                     -> 'callback_query.from'    : to get information about the user. Returns a 'User' class 
    #                                                   instance/object that contains details about the use
    #                     -> etc.
    callback_query = update.callback_query.data
    update.callback_query.answer()

    global likes
    global dislikes

    if callback_query == 'like':
        likes += 1

    if callback_query == 'dislike':
        dislikes += 1

    print(f'likes => {likes} and dislikes => {dislikes}')


# This is how map the self-made Python functions to the desired Handlers, and then add these mapped Handlers 
# to the 'Dispatcher' class instance/object of the Telegram Bot (which routes incoming updates (e.g. texts, 
# commands) from users/other Telegram Bots from the Telegram messaging platform server to the appropriate 
# Handler based on the type of update received). 

# CallbackQueryHandler is a Handler that Handles callbacks from inline keyboards.

# Here is a breakdown of the code:
# - Mapping the self-made Python function, 'handle_callback_query_python_function', to the desired Handler (which is 
#   CallbackQueryHandler in this case):
#           'telegram.ext.CallbackQueryHandler(handle_callback_query_python_function)'
# - Adding the mapped Handler to the 'Dispatcher' class instance/object of the Telegram Bot (which routes 
#   incoming updates (e.g. texts, commands) from users/other Telegram Bots from the Telegram messaging 
#   platform server to the appropriate Handler based on the type of update received):
#           'dispatcher.add_handler(telegram.ext.CallbackQueryHandler(telegram.ext.Filters.text, handle_callback_query_python_function))'
dispatcher.add_handler(telegram.ext.CallbackQueryHandler(handle_callback_query_python_function))


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
