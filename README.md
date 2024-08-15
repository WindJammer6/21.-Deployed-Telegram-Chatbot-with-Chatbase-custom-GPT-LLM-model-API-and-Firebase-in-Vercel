# 21.-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase <img src="https://logodownload.org/wp-content/uploads/2017/11/telegram-logo-8.png" width="50" height="50"> ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=chatgpt) ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=firebase)

This is a project done as part of my University's Undergraduate Research Opportunities Programme (UROP), titled 'UROP: Telegram chatbot for novice programmers to learn coding', supervised and initiated by Professor Oka Kurniawan ([here](https://github.com/kurniawano) is his Github account), spanding 8 months of (on-off) work.

Here is the description of the UROP project:  
'''  
Learning coding can be improved significantly when learners have an immediate and personalized feedback. The number of learners for coding make it impossible for human instructors to give an immediate and personalized feedback to learners. The rise of AI gives us the possibility to create a chatbot Tutor that can support learners anywhere and at any time. The purpose of this project is to create a Telegram chatbot where learners can get feedback related to their coding courses. The feedback should be accurate as reflected in the notes or instructor problem set.

The chatbot can be used for any institution that teaches programming.  
'''

This project is made up of 2 Github repositories:  
- [21.-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase](21.-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase) (this Github repository) (hosts the code for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database)
- Streamlit website

This Github repository is hosting the code for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database.

<br>

## My Approach to developing this UROP project:  
The approach is split into 2 components:  
1. Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database
  - Create a regular Telegram Bot -> integrating a Chatbase custom GPT LLM model to generate the Telegram Bot's responses to incoming texts/prompts from students (which basically gives the Telegram Bot the 'chatbot' functionality) -> incoming texts/prompts from students and the Chatbase custom GPT LLM model's responses will be saved into a database

2. Streamlit website 
  - There will be a separate website application containing 2 pages
    1. the first 'Details' page where it can take inputs from human instructors to manipulate the setting/behaviour of the Chatbase custom GPT LLM model via Prompt Engineering, and train the Chatbase custom GPT LLM model with their own course materials and notes without having to worry about their own course materials and notes leaking to the public
    2. the second 'Database' page where it displays the incoming texts/prompts from students and the Chatbase custom GPT LLM model's responses for the human instructors to evaluate the students' incoming texts/prompts (which the data is retrieved from the database)

*This project's deployed Telegram Bot, Chatbase custom GPT LLM model, Streamlit (Python Framework)'s Website Application and Firebase (API) links:*
+ https://t.me/test_12171_bot (Telegram Bot)
+ https://www.chatbase.co/dashboard/goh-jet-wei-team-91859289/chatbot/wGS8ehg-39TolweihWY3w (Direct link to this project's Chatbase custom GPT LLM model, but only accessible by me through email)
+ https://22-app-website-for-telegram-chatbot-hezsqgseuns85wxaqsdfpd.streamlit.app/ (Streamlit (Python Framework)'s Website Application)
+ https://console.firebase.google.com/u/0/project/urop-telegram-chatbot/database/urop-telegram-chatbot-default-rtdb/data (Direct link to this project's Firebase (API) Realtime database, but only accessible by me through email)

<br>

## Table of Contents
Here is a directory to explain the purpose of each file in this repository that is required in the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, as well as how to deploy a Telegram Bot on Vercel:
1. '.streamlit' folder  
   i. 'config.toml' file
2. 'README.md' file
3. 'firebase_key.json' file
4. 'karaoke_singer_class.py' file
5. 'requirements.txt' file

Additional files that are not part of the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, but includes the past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database:  
1.


Additional files that are not part of the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, but includes my learning journey of some of the required technology being used in this project that I was not familiar with:  
1.

1. How to deploy a Telegram Bot on Vercel? (can refer to the Unity Github repo on how I format the deployment documentation)


<br>

### Past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database
Due to my lack of knowledge in some of the required technology being used in the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, I had to first learn them, which includes:
- Building a Telegram Bot in Python (using the 'telegram.ext' (Python Framework) Telegram Bot API)
- Using Chatbase API

<br>

### My learning journey of some of the required technology being used in this project that I was not familiar with


