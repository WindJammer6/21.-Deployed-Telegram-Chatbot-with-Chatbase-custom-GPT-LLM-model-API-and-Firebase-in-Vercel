# The initiated Telegram Bot in this file in the Telegram messaging platform has the following information:
# - Name: Telegram_Chatbot_integrated_with_Chatbase_GPT_model_API_test
# - Username: test_12173_bot
# - API token/key: 7045977515:AAGGa78vjXmfTDzMPoCAkm2NsGpiYOi5WzI
# - Link of this Telegram Bot: https://t.me/test_12173_bot

# The goal of this Telegram Bot is to test the integration of the Chatbase custom GPT model API (Large
# Language Model (LLM) to a Telegram Bot.

# Chatbase custom GPT model API documentation: https://docs.chatbase.co/docs/create-a-chatbot 


# ////////////////////////////////////////////////////////////////////////////////////


# Workflow idea:
# 1. User Starts the Workflow
#    - User: /start
#    - Bot:
#      "👋 Hello there! Welcome to your friendly Teaching Assistant Telegram Bot, powered by the magic of Chatbase's custom GPT model API! 🌟
#       (A big shoutout to Goh Jet Wei (WindJammer6) for making this happen!)

#       You're now connected with the Teaching Assistant for SUTD's Computational Thinking and Design (CTD) (10.014) course. 🎓📘
#       (Psst... Just so you know, this conversation will be recorded for your instructors to help improve your learning!)

#       First things first, could you kindly enter your student ID so we can get started? 📝"
#    - Options: --Allow free text--

# 2. User enters Student ID
#    - User: --Entered student ID--
#    - Bot:
#      "Nice to meet you, student ID: --student id--! 🤩

#       Now, let's get down to business. Which assignment would you like to submit today? 📋
#       Select from the list below and let's roll! ⬇️"

#    - Options: [List of available assignments]

# 2. User Selects Assignment
#      - User: --Selected assignment--
#      - Bot:
#        "📝 You picked --Selected assignment--. Great choice! 🎯

#         Here’s everything you need to know about this assignment: [link to the selected assignment]

#         Ready to proceed? Let me know what you’d like to do next:"

#     - Options: Proceed to code submission (*Let’s dive right into submitting your code! 💻✨)


# 3. User Clicks 'Proceed to Code Submission'
#      - User: --Click Proceed to code submission--
#      - Bot:
#        "Awesome! 🛠️ Time to get those gears turning. Please go ahead and send me your working code when you're ready.
#         I’m excited to see what you've got! 🚀💡"

#      - Options: --Allow free text--

# 4. User submits their working code
#    - User: --Entered working code--
#    - Bot:
#      "🎉 Thanks for sharing your code! Here's a quick recap of everything you've provided:

#       📌 Student ID: --student id--
#       📌 Assignment: --Selected assignment--
#       📌 Code: --Entered working code--

#       Looking good? Ready to submit it for evaluation? 😄"

#    - Options: Submit code! (*Off it goes! ✈️ Let's get this evaluated.)
#               Restart

# 4.1. User Clicks 'Submit Code!'
#    - User: --Click Submit code--
#    - Bot:
#      "⏳ Give me a second while I work my magic and analyze your submission… 🙏

#       [5-second pause]

#       🎉 All done! Here’s the feedback for your submission to --Selected assignment--:

#       [Response from Chatbase GPT Model]

#       If you'd like to submit for another assignment, feel free to restart with the /start command anytime!
#       I’m here whenever you need me! 😁🤖"

# 4.2. User Clicks 'Restart'
#      - User: Restart
#      - Bot:
#        "🔄 No worries, just send me the updated version of your code when you're ready.
#         Let's make it perfect! 💪"


# ////////////////////////////////////////////////////////////////////////////////////


# (Random notes: 
# - Throughout the whole thing the inline keyboard must be blocked! And the buttons will show there in place 
#   of the keyboard! The button shouldn't be in the text bah I think thatll be better
# - I think can also remove any extra commands since they don't matter and complicate things such as the /help 
#   function idt we need it
# - and I guess for v3 there is no need for message handler anymore, unlike v2, which uses message handler for 
#   it to work, but v3 uses the inputs from the students to generate the response which will be the feedback
# - Rmb to type that in telegram bot it will only show the assignment but not the question, the question they 
#   might need to refer to somewhere else like another piece of paper or website...
# - Cuz if Telegram bot need show the full question might be too long alr
# )


# ////////////////////////////////////////////////////////////////////////////////////


# Professor Oka Kurniawan's comments:
# - add the link to the assignment question, or maybe can try pop ups if the Telegram Bot (Python) library allows 
#   so that students using the Telegram Chatbot have a reference to the assignment question before submitting
#   their codes
# - ensure that the student's responses have an identification of the student either using the student ID or 
#   the student's telegram handle
# - create 2 final versions of the telegram chatbot. One that has controlled input (using buttons) and another with 
#   free input, but relies on the LLM's ability to interpret the user's messages to extract the required information
#   (which should be the 3 things: student id, assignment id, and submitted code for the assignment)
#   -> Drawback to this is the worry that the LLM might hallucinate and generate unexpected replies... requires 
#      testing 
#   -> Possible system prompt for the LLM: 
#      '''
#      You are a university teaching assistant. Find the 3 important information in the student's message history, 
#      student id, assignment id, and submitted code for the assignment. 
     
#      If the student has provided all 3 important information, compile their information into the following format:
#      Student ID: 
#      Assignment ID:
#      Submitted code:
      
#      Test cases for the assignment:
#      Test cases failed for the assignment:
#      Test cases score for the assignment:
#      Recommended changes/advice to the Python code: 

#      Else, prompt the student for their response for the missing important information     
#      '''

#      The idea of the formatted response from the LLM is so that can extract the information only when the 3 important
#      information is provided, so that it will only be displayed in the Streamlit website when all 3 important
#      information is provided (to prevent spam and unexpected records in the Streamlit website database)


# ////////////////////////////////////////////////////////////////////////////////////


# Some extra ideas for the Telegram Chatbot (using Firebase)(cloud) v2:
# - Actually there might not even need to be 2 databases... just 1 will do. THe data can be stored as a dictionary in this format:
#   dict = { 'Assignment 1 - Two Sum' : [{Student ID:1007655, Student prompt:Testest, Chatbot response:Hello, nice to meet you}, {Student ID:1007658, Student prompt:What a function, Chatbot response:Its a wrapper}] , 'Assignment 2 - Longest string' : [{Student ID:1007678, Student prompt:Testest, Chatbot response:Hello, nice to meet you},{Student ID:1007623, Student prompt:Testest, Chatbot response:Hello, nice to meet you}] }

#   So that makes it easier for the transfer page too from one assignment to another in the website to view the respective list of prompts for that particular assignment!

# - Get the assignment link also as the input for the st.popover assignment in the streamlit website
# -  Maybe for the telegram bot see if can add an additional message below the image with the current likes and then update that message whenever the like or dislike button is clicked? See if that's possible
# -  For streamlit website can add a search bar at the sidebar to search filter according to student id instead of assignments id
#    To meet the comment mentioned by prof oka

# - add the /help function in the /start command too to show got cancel command oso



import telegram
import telegram.ext
import json
import requests
import time
from firebase_admin import db
import firebase_admin
import datetime


# Initiating Chatbase stuffs
url = 'https://www.chatbase.co/api/v1/chat'

headers = {
    'Authorization': 'Bearer 3c7b798b-c5fe-41a7-bdeb-f5d0b6f8536e',
    'Content-Type': 'application/json'
}

conversation_history_and_other_data = {
    "messages": [],
    "chatbotId": "wGS8ehg-39TolweihWY3w",
    "stream": False,
    "temperature": 0
}


# Initiating multiple Firebase Realtime Database/projects in the same Python file

# Setting up the Firebase database for the conversations:

#Here is the link that goes directly to this UROP Telegram Chatbot project's Firebase Realtime database:
#https://console.firebase.google.com/u/0/project/urop-telegram-chatbot/database/urop-telegram-chatbot-default-rtdb/data

#This if statement, accompanied by the condition with the function 'firebase_admin._apps', is used to prevent
#any error from creating multiple Firebase apps with the same name. 

#The 'firebase_app = firebase_admin.initialize_app' within this if statement will instantiate a Firebase app 
#if it is not already created, which is what the 'firebase_admin._apps' does, as an internal variable that 
#keeps track of the initialized Firebase apps. It is a dictionary-like object that holds information about 
#the Firebase apps that have been initialized in your Python application.
if "conversations" not in firebase_admin._apps:
    # Initialize Firebase
    credentials_object_conversations = firebase_admin.credentials.Certificate("firebase_key_conversations.json")
    firebase_admin.initialize_app(credentials_object_conversations, {
        'databaseURL': 'https://urop-telegram-chatbot-default-rtdb.asia-southeast1.firebasedatabase.app/'
    }, name='conversations')

# Get a reference to the database
reference_to_database_conversations = db.reference('/', app=firebase_admin.get_app('conversations'))



# Setting up the Firebase database for the assignments:

# Here is the link that goes directly to this UROP Telegram Chatbot assignments's Firebase Realtime database:
# https://console.firebase.google.com/u/0/project/urop-chatbot-assignments/database/urop-chatbot-assignments-default-rtdb/data

# This if statement, accompanied by the condition with the function 'firebase_admin._apps', is used to prevent
# any error from creating multiple Firebase apps with the same name. 

# The 'firebase_app = firebase_admin.initialize_app' within this if statement will instantiate a Firebase app 
# if it is not already created, which is what the 'firebase_admin._apps' does, as an internal variable that 
# keeps track of the initialized Firebase apps. It is a dictionary-like object that holds information about 
# the Firebase apps that have been initialized in your Python application.    
if "assignments" not in firebase_admin._apps:
    # Initialize Firebase
    credentials_object_assignments = firebase_admin.credentials.Certificate("firebase_key_assignments.json")
    firebase_admin.initialize_app(credentials_object_assignments, {
        'databaseURL': 'https://urop-chatbot-assignments-default-rtdb.asia-southeast1.firebasedatabase.app/'
    }, name='assignments')

# Get a reference to the database
reference_to_database_assignments = db.reference('/', app=firebase_admin.get_app('assignments'))


# Firebase's Database for conversations to Streamlit website things:
# Compiling the list of available assignments from the Streamlit (Python) website to Keyboard buttons in the
# Telegram Chatbot 

# Read data from the Realtime Database from Firebase
database_data_assignments = reference_to_database_assignments.get()
# print("Firebase UROP Telegram Chatbot assignments Realtime Database Data:", database_data_assignments)

list_of_assignments = []

# Check if the Firebase Realtime database is None or empty
if database_data_assignments is None:
    print("No data found in the Firebase Realtime Database.")
else:
    # Converting the Firebase Realtime Database to a list of dictionaries
    if isinstance(database_data_assignments, dict):
        database_data_assignments = list(database_data_assignments.values())

        print(database_data_assignments)

    for i in range(len(database_data_assignments)):
        list_of_assignments.append(f"{database_data_assignments[i]['assignment_name']}")




# ////////////////////////////////////////////////////////////////////////////////////


# This part of the code is to fix the issue where when an assignment is added/removed from the UROP Telegram Chatbot assignments's 
# Firebase Realtime database from the Streamlit website, the assignment keyboard buttons in the custom keyboard in the Telegram
# Bot is not updated while the Telegram Bot is running. 

# These codes solves this issue by allowing the assignment keyboard buttons in the custom keyboard in the Telegram Bot to be 
# updated while the Telegram Bot is running, by getting the Telegram Bot to poll periodically from the UROP Telegram Chatbot 
# assignments's Firebase Realtime database, and updates the assignment keyboard buttons in the custom keyboard in the Telegram Bot 
# to be updated while the Telegram Bot is running if there is any changes made to the UROP Telegram Chatbot assignments's 
# Firebase Realtime database (e.g. an assignment is added/removed from the UROP Telegram Chatbot assignments's Firebase Realtime 
# database from the Streamlit website)

# (Note: The main function, 'check_for_new_data()' is below the 'updater.start_polling()' function at the bottom of the
# code)
def get_firebase_data():


    # ////////////////////////////////////////////////////////////////////////////////


    # Firebase's Database for conversations to Streamlit website things:
    # Compiling the list of available assignments from the Streamlit (Python) website to Keyboard buttons in the
    # Telegram Chatbot 

    # Read data from the Realtime Database from Firebase
    database_data_assignments = reference_to_database_assignments.get()
    # print("Firebase UROP Telegram Chatbot assignments Realtime Database Data:", database_data_assignments)

    list_of_assignments = []

    # Check if the Firebase Realtime database is None or empty
    if database_data_assignments is None:
        print("No data found in the Firebase Realtime Database.")
    else:
        # Converting the Firebase Realtime Database to a list of dictionaries
        if isinstance(database_data_assignments, dict):
            database_data_assignments = list(database_data_assignments.values())

            print(database_data_assignments)

        for i in range(len(database_data_assignments)):
            list_of_assignments.append(f"{database_data_assignments[i]['assignment_name']}")

    
    # ////////////////////////////////////////////////////////////////////////////////

    
    return list_of_assignments


def build_keyboard(list_of_assignments):
    keyboard_buttons = []
    if list_of_assignments is not None:
        keyboard_buttons = []
        
        for i in list_of_assignments:
            keyboard_buttons.append([telegram.KeyboardButton(i)])

    return telegram.ReplyKeyboardMarkup(keyboard_buttons)


def check_for_new_data(updater):
    old_data = get_firebase_data()

    while True:
        time.sleep(10)  # Poll Firebase every 10 seconds
        new_data = get_firebase_data()

        if new_data != old_data:
            # Update the buttons if new data is found
            for chat_id in updater.dispatcher.chat_data:
                keyboard = build_keyboard(new_data)
                updater.bot.send_message(chat_id=chat_id, text="Oops! There is an update to the assignments available from your course instructor!", reply_markup=keyboard)
            
            old_data = new_data  # Update old_data to the new state
            print(old_data)


# ////////////////////////////////////////////////////////////////////////////////////




# Defining the states for the conversation with the Telegram Chatbot
ASK_STUDENTID, ASK_ASSIGNMENT, ASK_CODE_SUBMISSION = range(3)

# Storing the information received from the student during the conversation, it should contain the
# 3 rquired information, student ID, selected assignment, and code to be submitted
CONVERSATION_INFORMATION = {} 


def handle_start_command_python_function(update, context):
    print("Start command received")  # Add this line to verify if the command is being received
    
    # Reset the conversation information
    CONVERSATION_INFORMATION.clear()


    # Sending an image of a Telegram Chatbot teaching assistant
    image = requests.get('https://static05.cminds.com/wp-content/uploads/WP_Telegram_Bot_Plugin_Illustravive_Banner-1024x300.jpg').content
    update.message.reply_media_group(media=[telegram.InputMediaPhoto(image, caption="""👋 Hello there! Welcome to your friendly Teaching Assistant Telegram Bot, powered by the magic of Chatbase's custom GPT model API! 🌟\n(A big shoutout to Goh Jet Wei (WindJammer6) for making this happen!)\n\nYou're now connected with the Teaching Assistant for SUTD's Computational Thinking and Design (CTD) (10.014) course. 🎓📘\n(Psst... Just so you know, this conversation will be recorded for your instructors to help improve your learning!)\n\nFirst things first, could you kindly enter your student ID so we can get started? 📝""")])
    
    return ASK_STUDENTID


# Start command + Asking of the student id information
def handle_ask_studentid_messages_python_function(update, context):
    student_id = update.message.text

    # Very sketchy code
    if 'code_submitted' in CONVERSATION_INFORMATION:
        value = CONVERSATION_INFORMATION['code_submitted']
        CONVERSATION_INFORMATION.clear()
        CONVERSATION_INFORMATION['student_id'] = value
        print(CONVERSATION_INFORMATION)
    else:
        CONVERSATION_INFORMATION['student_id'] = student_id
        print(CONVERSATION_INFORMATION)
    

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    # Firebase's Database for conversations to Streamlit website things

    # Compiling the list of available assignments from the Streamlit (Python) website to Keyboard buttons in the
    # Telegram Chatbot (see above to see how the 'list_of_assignments' variable is derived)

    if list_of_assignments is not None:
        keyboard_buttons = []
        
        for i in list_of_assignments:
            keyboard_buttons.append([telegram.KeyboardButton(i)])


    # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    update.message.reply_text(f"""
                              Nice to meet you, student ID: {CONVERSATION_INFORMATION['student_id']}!\n\nNow, let's get down to business. Which assignment would you like to submit today? 📋"
                              """
                              , reply_markup=telegram.ReplyKeyboardMarkup(keyboard_buttons, one_time_keyboard=True))
    
    return ASK_ASSIGNMENT


# Asking of the assignment information
def handle_ask_assignment_messages_python_function(update, context):
    assignment = update.message.text
    CONVERSATION_INFORMATION['assignment'] = assignment
    print(CONVERSATION_INFORMATION)
    
    inline_keyboard_buttons = [[telegram.InlineKeyboardButton("Proceed to code submission", callback_data="proceed_to_code_submission")]]


    # ////////////////////////////////////////////////////////////////////////////////////


    # To extract the assignment link for the extracted assignment name in the 'list_of_assignments' list
    extracted_assignment_link = None

    for assignment in database_data_assignments:
        if assignment['assignment_name'] == CONVERSATION_INFORMATION['assignment']:
            extracted_assignment_link = assignment['assignment_link']

    
    # ////////////////////////////////////////////////////////////////////////////////////

    
    update.message.reply_text(f"""
                               📝 You picked {CONVERSATION_INFORMATION['assignment']}.\n\nHere’s everything you need to know about this assignment: {extracted_assignment_link}\n\nReady to proceed? Let me know what you’d like to do next:\n\n\nIf you'd like to submit for another assignment, feel free to restart with the /start command anytime! I’m here whenever you need me! 😁🤖
                               """
                               , reply_markup=telegram.InlineKeyboardMarkup(inline_keyboard_buttons, one_time_keyboard=True))

    return ASK_CODE_SUBMISSION


# Confirmation of all 3 information (student id, assignment and code submitted) before submission
def handle_ask_code_submission_messages_python_function(update, context):
    code_submitted = update.message.text  
    CONVERSATION_INFORMATION['code_submitted'] = code_submitted
    print(CONVERSATION_INFORMATION)

    # Very sketchy code
    if 'student_id' not in CONVERSATION_INFORMATION:
        return handle_ask_studentid_messages_python_function(update, context)
    else:
        # if 'student_id' not in CONVERSATION_INFORMATION:
        #     update.message.reply_text("Error: Student ID is missing.")
        #     return ASK_STUDENTID

        inline_keyboard_buttons = [[telegram.InlineKeyboardButton("Submit code", callback_data="submit_code")], [telegram.InlineKeyboardButton("Restart", callback_data="restart")]]

        update.message.reply_text(f"""
                                "🎉 Thanks for sharing your code! Here's a quick recap of everything you've provided:\n\n📌 Student ID: {CONVERSATION_INFORMATION['student_id']}\n📌 Assignment: {CONVERSATION_INFORMATION['assignment']}\n📌 Code:\n{CONVERSATION_INFORMATION['code_submitted']}\n\nLooking good? Ready to submit it for evaluation? 😄
                                """, reply_markup=telegram.InlineKeyboardMarkup(inline_keyboard_buttons, one_time_keyboard=True))


# Displaying response from Chatbase custom GPT LLM model
def telegram_chatbot_chatbase_response_to_code_submission_python_function(update, context):
    # Appending the user message/prompt to the 'conversation_history_and_other_data' before making the API call
    conversation_history_and_other_data["messages"].append({"content": update.message.text, "role": "user"})

    # Generating the Chatbase custom GPT response to the user message/prompt when making the API call
    response = requests.post(url, headers=headers, data=json.dumps(conversation_history_and_other_data))
    json_data = response.json()

    # If there is no error generating the Chatbase custom GPT response
    if response.status_code == 200:
        # Appending the generated Chatbase custom GPT response to the 'conversation_history_and_other_data' 
        conversation_history_and_other_data["messages"].append({"content": json_data['text'], "role": "assistant"})
        print(conversation_history_and_other_data["messages"])

        update.message.reply_text("""
                                  ⏳ Give me a second while I work my magic and analyze your submission… 🙏 
                                  """)
        time.sleep(3)
        update.message.reply_text(f"""
                                  🎉 All done! Here’s the feedback for your submission to {CONVERSATION_INFORMATION['assignment']}.\n\n(Your submission has been recorded).
                                  """)    
        update.message.reply_text(f"""
                                  Chatbase custom GPT model:\n\n{json_data['text']}
                                  """)     
        
        inline_keyboard_buttons = [[telegram.InlineKeyboardButton("Restart", callback_data="restart")]]
        update.message.reply_text(f"""
                                  If you'd like to submit for another assignment, feel free to click restart! I’m here whenever you need me! 😁🤖
                                  """, reply_markup=telegram.InlineKeyboardMarkup(inline_keyboard_buttons, one_time_keyboard=True))     
        

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////
        

        # Telegram Chatbot to Firebase's Realtime Database things

        # Adding Chatbase response to each submission into each submission data
        CONVERSATION_INFORMATION['telegram_chatbot_chatbase_response'] = f"```\n{json_data['text']}\n```"
        print(CONVERSATION_INFORMATION)


        # Adding date and time information of the submission to each submission data
        date_and_time_of_submission = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        CONVERSATION_INFORMATION['date_and_time_of_submission'] = date_and_time_of_submission
        print(CONVERSATION_INFORMATION)


        # Once the code is submitted by the user, the Telegram Chatbot will 'push' basically add these new pieces of user data 
        # into the Realtime database in Firebase
        reference_to_database_conversations.push(CONVERSATION_INFORMATION)    


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////
        

    # If there is an error when generating the Chatbase custom GPT response for some reason
    else:
        print(f"Error: {json_data}")
        update.message.reply_text(f"Chatbase custom GPT model: Oh no! You encountered an error in the code! The error is: \n'{json_data['message']}'")
        
    
    return telegram.ext.ConversationHandler.END


# Handling callback queries from the Inline Keyboard Buttons
def handle_callback_queries(update, context):
    callback_query = update.callback_query
    callback_query.answer()

    # Handling assignment selection callback
    if callback_query.data == 'proceed_to_code_submission':
        callback_query.message.reply_text("Awesome! 🛠️ Time to get those gears turning. Please go ahead and send me your working code when you're ready.\nI’m excited to see what you've got! 🚀💡")
        return ASK_CODE_SUBMISSION

    # Handling code submission callback
    elif callback_query.data == 'submit_code':
        return telegram_chatbot_chatbase_response_to_code_submission_python_function(callback_query, context)

    # Handling restart submission callback
    elif callback_query.data == 'restart':
        handle_start_command_python_function(callback_query, context)
        return ASK_STUDENTID

# Cancel function here to map to the cancel command as per required by the telegram Python library's 
# 'ConversationHandler' class instance/object 
def cancel(update, context):
    update.message.reply_text(
        'Conversation cancelled.',
        reply_markup=telegram.ReplyKeyboardRemove()
    )
    return telegram.ext.ConversationHandler.END


# Initiate the Telegram Chatbot
token_of_telegram_bot = "6671076375:AAGIvph3qscPLo1bQmcNPrI2W9mhu4c2vv4"
updater = telegram.ext.Updater(token_of_telegram_bot, use_context=True)
dispatcher = updater.dispatcher



# Handlers
conversation_handler = telegram.ext.ConversationHandler(
    entry_points=[telegram.ext.CommandHandler('start', handle_start_command_python_function)],
    states={
        ASK_STUDENTID: [telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_ask_studentid_messages_python_function)],
        ASK_ASSIGNMENT: [telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_ask_assignment_messages_python_function)],
        ASK_CODE_SUBMISSION: [telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_ask_code_submission_messages_python_function)]
    },
    fallbacks=[telegram.ext.CommandHandler('cancel', cancel)]
)

dispatcher.add_handler(conversation_handler)
dispatcher.add_handler(telegram.ext.CallbackQueryHandler(handle_callback_queries))


# Start the Telegram Chatbot
updater.start_polling()

# The 'check_for_new_data()' self-made function (see above)
check_for_new_data(updater)

updater.idle()
