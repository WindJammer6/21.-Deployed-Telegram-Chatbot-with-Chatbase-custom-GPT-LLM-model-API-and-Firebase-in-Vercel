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
# We will also be using the 'requests' Python library to retrieve information from 2 different websites
# (see the '911. telegram's_InlineKeyboardButton_class_and_InlineKeyboardMarkup_class.py' file).
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

    # To create the keyboard buttons, 'Random Person's Face' or 'Random Thing' in the telegram bot 
    # keyboard, you will need to use the telegram (Python) library's 'KeyboardButton' class and 
    # 'ReplyKeyboardMarkup' class, and here is what each of them do respectiuvely:
    # - 'KeyboardButton' class      - represents a single button in a custom reply telegram bot keyboard. This
    #                                 button can be used to send predefined replies to the telegram bot when 
    #                                 pressed 
    # - 'ReplyKeyboardMarkup' class - used to display a custom reply keyboard. This custom reply keyboard is
    #                                 meant to replace the default keyboard and can contain features such as
    #                                 keyboard buttons created by the 'KeyboardButton' class

    # Creating the keyboard buttons using the telegram (Python) library's 'KeyboardButton' class
    keyboard_buttons = [[telegram.KeyboardButton("Random Person's Face")], [telegram.KeyboardButton("Random Thing")]] 
    

    # Creating the custom reply keyboard using the telegram (Python) library's 'ReplyKeyboardMarkup' class,
    # and putting it as an input of the 'reply_markup' parameter of the 'reply_text()' instance method
    # in the 'Message' class instance/object

    # (Note: There is an additional 'reply_markup' parameter being used in the 'reply_text()' instance method 
    #  in the 'Message' class instance/object here. See what it does in the '6. creating_self-made_Python_
    #  functions.py' file)
    update.message.reply_text("Hello, welcome to my random image posts telegram bot! (From WindJammer6)", reply_markup=telegram.ReplyKeyboardMarkup(keyboard_buttons))
    # This works too:
    # context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, welcome to my random image posts telegram bot! (From WindJammer6)", reply_markup=telegram.ReplyKeyboardMarkup(keyboard_buttons))


    # What does the 'context.bot.send_message()' code do?
    # The 'context.bot.send_message()' code is another way to send a text message as a reply to the message sender.

    # Here is a breakdown of the 'context.bot.send_message()' code:
    # - 'context': represents additional contextual information and functionality to the Handler. It is a class 
    #              instance/object that contains various attributes and methods to interact with the Telegram Bot's 
    #              environment and Telegram API. For example, it provides methods to send messages, access user 
    #              data, manage conversation states, and more. (refer to the '7. What_are_Handlers.txt'
    #              file for more about what are Handlers in the context of the 'telegram.ext' Telegram Bot API 
    #              Python Framework) (it is the second parameter in the self-made Python functions that will give 
    #              the Telegram Bot its functionalities (refer to the '6. creating_self-made_Python_functions.py' 
    #              file))
    # - 'bot'    : represents the Telegram Bot class instance associated with the class instance/object that the 
    #              'context' code is representing                        
    # - 'send_message()': This is an instance method in the Telegram Bot class instance/object that will send a text 
    #                     reply message as a reply to the message sender in a specific chat in the Telegram Bot, which
    #                     you can specify using the 'chat_id' parameter (see below). It takes in many parameters, but 
    #                     3 of the most common ones are:
    #                     -> 'chat_id'      - represents the specific chat in the Telegram Bot to send a text reply
    #                                         message as a reply to the message sender. You can retrieve identification 
    #                                         information of the specific chat in the Telegram Bot using the code:
    #                                         'update.effective_chat.id' by letting this code be the input of this
    #                                         parameter
    #                     -> 'text'         - the text of the message to send
    #                     -> 'reply_markup' - adds interactive elements such as inline keyboard buttons and keyboard
    #                                         buttons that you can use instead to send a text reply to the meesage
    #                                         (you can see how this is done in the '910. telegram's_KeyboardButton_
    #                                         class_and_ReplyKeyboardMarkup_class.py' file)


    # How is the 'context.bot.send_message()' code different from the 'update.message.reply_text()' code?
    # Both does the same thing which is both are used to send messages to users in Telegram Bot interactions

    # The only difference is that the 'context.bot.send_message()' code offers an additional functionality by allowing
    # you to specify which chat in the Telegram Bot to send the message to, while the 'update.message.reply_text()' code
    # is shorter, and is just programmed to just send the message to the same chat of the conversation in the Telegram Bot.



# Mapping the self-made Python functions to the CommandHandler (note that there are many other kinds of 
# Handlers in the 'telegram.ext' Telegram Bot API Python Framework that can handle different types of updates)

# CommandHandler is a Handler that Handles commands sent by users.
dispatcher.add_handler(telegram.ext.CommandHandler('start', start_python_function))


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