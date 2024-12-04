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
#    - Bot: "Hello, welcome to my telegram chatbot integrated with Chatbase custom GPT model API! 
#           (From Goh Jet Wei (WindJammer6)) 
#           
#           This is the Teaching Assistant Telegram Chatbot for SUTD's Computational Thinking and 
#           Design (CTD) (10.014) course. Note that this conversation will be recorded for SUTD
#           instructors to facilitate teaching.
#
#           Enter your student ID:
#           "
#    - Options: --Allow free text--

# 2. User enters their student ID
#    - User: --Entered student ID--
#    - Bot: "
#           Hello, student with student ID --student id--!

#           Select your assignment to submit for the course:
#           "
#    - Options: [List of available assignments]

# 2. User selected an assignment
#    - User: --Selected assignment-- (e.g. 'Assignment 1 - Two Sum')
#    - Bot: "
#           You chose --Selected assignment--. 

#           Here is the information of the assignment: --link to the selected assignment-- 

#           Confirm?"
#           "
#    - Options: Proceed to code submission (with a button that links to the code submission), 
#               Reselect assignment (with a button to go back to assignment selection)

# 2.1. User Clicks 'Proceed to code submission'
#      - User: Clicks "Proceed to code submission"
#      - Bot: "Please enter and send your working code:"
#      - Options: --Allow free text--

# 2.2. User Clicks 'Reselect assignment'
#      - User: Clicks "Reselect assignment"
#      - Bot: "
#             Hello, student with student ID --student id--!

#             Select your assignment to submit for the course:
#             "
#      - Options: [List of available assignments]

# 3. User submits their working code
#    - User: --Entered working code--
#    - Bot: "
#           Thank you for your code submission! 

#           Here is the information you provided.
#           Student ID: --student id--
#           Assignment ID selected: --Selected assignment--
#           Code to be submitted: --Entered working code--

#           Confirm submission?
#           "
#      - Options: Submit code! (with a button that links to the submit code), 
#                 Resubmit code (with a button to go back to code submission)

# 3.1. User clicks 'Submit code!'
#      - User: Clicks 'Submit code!
#      - Bot: 
#           "
#           Give me a moment to analyse your code 🙏. 
#           "

#           [--can add a 5 seconds 'time.sleep()' function in the code here--]

#           "           
#           Thank you for waiting! Here is the feedback of your code submission for the assignment: 
#           --Selected assignment--
#           "

#           "
#           --shows response of Chatbase custom GPT LLM model--
#           " 

#           "
#           If you would like to submit for another assignement, please rerun the '/start' command 😁
#           "

# 3.2. User clicks 'Resubmit code'
#      - User: Clicks 'Resubmit code'
#      - Bot: "Please enter and send your working code:"
#      - Options: --Allow free text--


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

# add the /help function in the /start command too to show got cancel command oso



import telegram
import telegram.ext
import json
import requests
import time
from firebase_admin import db
import firebase_admin


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


# Defining the states for the conversation with the Telegram Chatbot
ASK_STUDENTID, ASK_ASSIGNMENT, ASK_CODE_SUBMISSION = range(3)

# Storing the information received from the student during the conversation, it should contain the
# 3 rquired information, student ID, selected assignment, and code to be submitted
CONVERSATION_INFORMATION = {} 


def handle_start_command_python_function(update, context):
    print("Start command received")  # Add this line to verify if the command is being received
    update.message.reply_text("""
                              Hello, welcome to my telegram bot integrated with Chatbase custom GPT model API! (From Goh Jet Wei (WindJammer6)\n\nThis is the Teaching Assistant Telegram Chatbot for SUTD's Computational Thinking and Design (CTD) (10.014) course. Note that this conversation will be recorded for SUTD instructors to facilitate teaching.\n\nEnter your student ID:
                              """)
    return ASK_STUDENTID


# Start command + Asking of the student id information
def handle_ask_studentid_messages_python_function(update, context):
    student_id = update.message.text
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
                                Hello, student with student ID: {CONVERSATION_INFORMATION['student_id']}!\n\nSelect your assignment to submit for the course:
                                """
                                , reply_markup=telegram.ReplyKeyboardMarkup(keyboard_buttons, one_time_keyboard=True))
    
    return ASK_ASSIGNMENT


# Asking of the assignment information
def handle_ask_assignment_messages_python_function(update, context):
    assignment_id = update.message.text
    CONVERSATION_INFORMATION['assignment_id'] = assignment_id
    print(CONVERSATION_INFORMATION)
    
    inline_keyboard_buttons = [[telegram.InlineKeyboardButton("Proceed to code submission", callback_data="proceed_to_code_submission")], [telegram.InlineKeyboardButton("Reselect assignment", callback_data="reselect_assignment")]]

    
    # ////////////////////////////////////////////////////////////////////////////////////


    # To extract the assignment name from the "Assignment [assignment_id]: [assignment_name]" string:
    parts = CONVERSATION_INFORMATION['assignment_id'].split(':', 1)  # Split into two parts
    if len(parts) > 1:
        # Extract and strip any leading/trailing whitespace
        extracted_assignment_name = parts[1].strip()
        print(f"Extracted Assignment Name: {extracted_assignment_name}")
    else:
        print("No assignment name found")

    # To extract the assignment link for the extracted assignment name in the 'list_of_assignments' list
    extracted_assignment_link = None

    for assignment in database_data_assignments:
        print(assignment)
        if assignment['assignment_name'] == extracted_assignment_name:
            extracted_assignment_link = assignment['assignment_link']
        else:
            extracted_assignment_link = None

    
    # ////////////////////////////////////////////////////////////////////////////////////


    update.message.reply_text(f"""
                               You chose: {CONVERSATION_INFORMATION['assignment_id']}.\n\nHere is the information of the assignment: {extracted_assignment_link}\n\nConfirm?
                               """
                               , reply_markup=telegram.InlineKeyboardMarkup(inline_keyboard_buttons, one_time_keyboard=True))

    return ASK_CODE_SUBMISSION


# Confirmation of all 3 information (student id, assignment and code submitted) before submission
def handle_ask_code_submission_messages_python_function(update, context):
    code_submitted = update.message.text  
    CONVERSATION_INFORMATION['code_submitted'] = code_submitted
    print(CONVERSATION_INFORMATION)

    inline_keyboard_buttons = [[telegram.InlineKeyboardButton("Submit code", callback_data="submit_code")], [telegram.InlineKeyboardButton("Resubmit code", callback_data="resubmit_code")]]

    update.message.reply_text(f"""
                               Thank you for your code submission!\n\nHere is the information you provided.\nStudent ID: {CONVERSATION_INFORMATION['student_id']}\nAssignment selected: {CONVERSATION_INFORMATION['assignment_id']}\nCode to be submitted: {CONVERSATION_INFORMATION['code_submitted']}\n\nConfirm submit?
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
                                  Give me a moment to analyse your code 🙏... 
                                  """)
        time.sleep(2)
        update.message.reply_text(f"""
                                  Thank you for waiting! Here is the feedback of your code submission for the assignment: {CONVERSATION_INFORMATION['assignment_id']}.\n\n(Your submission has been recorded).
                                  """)    
        update.message.reply_text(f"""
                                  Chatbase custom GPT model:\n\n{json_data['text']}
                                  """)     
        update.message.reply_text(f"""
                                  If you would like to submit for another assignement, please rerun the '/start' command 😁
                                  """)     
        

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////
        

        # Telegram Chatbot to Firebase's Realtime Database things

        # Once the code is submitted by the user, the Telegram Chatbot will 'push' basically add this new pieces of user data 
        # into the Realtime database in Firebase    
        CONVERSATION_INFORMATION['telegram_chatbot_chatbase_response'] = json_data['text']
        print(CONVERSATION_INFORMATION)
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
        callback_query.message.reply_text("Please enter and send your working code:")
        return ASK_CODE_SUBMISSION

    elif callback_query.data == 'reselect_assignment':


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////


        # Firebase's Database for conversations to Streamlit website things

        # Compiling the list of available assignments from the Streamlit (Python) website to Keyboard buttons in the
        # Telegram Chatbot (see above to see how the 'list_of_assignments' variable is derived)

        if list_of_assignments is not None:
            keyboard_buttons = []
            
            for i in list_of_assignments:
                keyboard_buttons.append([telegram.KeyboardButton(i)])
            

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////


        callback_query.message.reply_text("Please select your assignment again:", reply_markup=telegram.ReplyKeyboardMarkup(keyboard_buttons, one_time_keyboard=True))
        return ASK_ASSIGNMENT
    

    # Handling code submission callback
    elif callback_query.data == 'submit_code':
        return telegram_chatbot_chatbase_response_to_code_submission_python_function(callback_query, context)

    elif callback_query.data == 'resubmit_code':
        callback_query.message.reply_text("Please resubmit your code:")
        return ASK_CODE_SUBMISSION


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
updater.idle()
