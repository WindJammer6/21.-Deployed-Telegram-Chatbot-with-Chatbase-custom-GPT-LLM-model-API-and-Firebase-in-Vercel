# Following this Youtube video by Simplilearn: https://www.youtube.com/watch?v=227uk4kDTM8 (Youtube video
# by Simplilearn, tiitled 'How To Create A Telegram Bot Using Python? | Telegram Bot In Python 
# Tutorial | Python | Simplilearn/')



# ///////////////////////////////////////////////////////////////////////////


# How to run Telegram Bot API (Python Framework) code and the Telegram Bot?
# First, you need to create a Telegram Bot in the Telegram messaging platform (refer to the 
# '2. How_to_create_a_Telegram_Bot.txt' file). 

# Then, the way to run Telegram Bot API (Python Framework) code is by pressing the triangle 'Run' button at 
# the top right of the screen.

# Then, to look at any changes in the Telegram Bot's API (Python Framework)'s code, refer to the Telegram 
# Bot's chat itself in the Telegram messaging platform and run the commands created to check the output of 
# the commands. The terminal in the IDE will show the errors in your Telegram Bot's API (Python Framework)
# code.

# (Note: The Telegram Bot will not respond to commands in the Telegram Bot's chat itself in the Telegram 
#        messaging platform if you did not run the Telegram Bot's API (Python Framework)'s code in the IDE)


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
