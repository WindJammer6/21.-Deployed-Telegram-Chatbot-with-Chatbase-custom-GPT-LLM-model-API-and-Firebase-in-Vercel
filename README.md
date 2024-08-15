# 21.-Deployed-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase <img src="https://logodownload.org/wp-content/uploads/2017/11/telegram-logo-8.png" width="50" height="50"> ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=chatgpt) ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=firebase) ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=vercel)

This is a project done as part of my University's Undergraduate Research Opportunities Programme (UROP), titled **'UROP: Telegram chatbot for novice programmers to learn coding'**, supervised and initiated by Professor Oka Kurniawan ([here](https://github.com/kurniawano) is his Github account), spanding 8 months of (on-off) work.

Here is the description of the UROP project:  
'''  
Learning coding can be improved significantly when learners have an immediate and personalized feedback. The number of learners for coding make it impossible for human instructors to give an immediate and personalized feedback to learners. The rise of AI gives us the possibility to create a chatbot Tutor that can support learners anywhere and at any time. The purpose of this project is to create a Telegram chatbot where learners can get feedback related to their coding courses. The feedback should be accurate as reflected in the notes or instructor problem set.

The chatbot can be used for any institution that teaches programming.  
'''

This project is made up of 2 Github repositories:  
- [21.-Deployed-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase](21.-Deployed-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase) (this Github repository) (hosts the code for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database)
- Streamlit website (the other repository)

This Github repository is hosting the code for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database.

<br>

## My Approach to developing this UROP project:  
The approach to developing this UROP project is split into 2 components:  
1. **Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database**
  - Create a regular Telegram Bot -> integrating a Chatbase custom GPT LLM model to generate the Telegram Bot's responses to incoming texts/prompts from students (which basically gives the Telegram Bot the 'chatbot' functionality) -> incoming texts/prompts from students and the Chatbase custom GPT LLM model's responses will be saved into a database

2. **Streamlit website** 
  - There will be a separate website application containing 2 pages
    1. the first 'Details' page where it can take inputs from human instructors to manipulate the setting/behaviour of the Chatbase custom GPT LLM model via Prompt Engineering, and train the Chatbase custom GPT LLM model with their own course materials and notes without having to worry about their own course materials and notes leaking to the public
    2. the second 'Database' page where it displays the incoming texts/prompts from students and the Chatbase custom GPT LLM model's responses for the human instructors to evaluate the students' incoming texts/prompts (which the data is retrieved from the database)

*This project's deployed Telegram Bot, Chatbase custom GPT LLM model, Streamlit (Python Framework)'s Website Application and Firebase (API) links:*
+ https://t.me/test_12171_bot (Telegram Bot)
+ https://www.chatbase.co/dashboard/goh-jet-wei-team-91859289/chatbot/wGS8ehg-39TolweihWY3w (Direct link to this project's Chatbase custom GPT LLM model, but only accessible by me through email)
+ https://22-app-website-for-telegram-chatbot-hezsqgseuns85wxaqsdfpd.streamlit.app/ (Streamlit (Python Framework)'s Website Application)
+ https://console.firebase.google.com/u/0/project/urop-telegram-chatbot/database/urop-telegram-chatbot-default-rtdb/data (Direct link to this project's Firebase (API) Realtime database, but only accessible by me through email)


Maybe add a how to use section? Saying that the Chatbase API part might require money to get access to the API key... and hence otherwise cannot be used??

<br>

## Table of Contents
Here is a directory to explain the purpose of each file in this repository:

1. Files that are required in the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database:
  1. '.streamlit' folder  
     i. 'config.toml' file
  2. 'README.md' file
  3. 'firebase_key.json' file
  4. 'karaoke_singer_class.py' file
  5. 'requirements.txt' file

2. Additional files that are not part of the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, but includes the past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database:  
  1.


3. Additional files that are not part of the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, but includes my learning journey of some of the required technology being used in this project that I was not familiar with:  
  1.

4. Deployment Process of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database (or any other Telegram Bots) on Vercel  

<br>

### 1. File that are required in the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database

<br>

### 2. Past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database
Telegram_bot.py is not required and is just merely for local running as long polling. (refer to the deployment process)

Wanted to

<br>

### 3. My learning journey of some of the required technology being used in this project that I was not familiar with
Due to my lack of knowledge in some of the required technology being used in the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, I had to first learn them, which includes:
- Building a Telegram Bot in Python (using the 'telegram.ext' (Python Framework) Telegram Bot API)
- Using Chatbase API (requires money)
- OpenAI API (but ended up not using it)

What is [Chatbase](https://www.chatbase.co/)?  
'Chatbase is an AI chatbot builder that allows companies and other users to create their own chatbot trained on their specific data, such as documentation or website content.'    
Source: https://www.techopedia.com/definition/chatbase (Techopedia)  

<br>

### 4. Deployment Process of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database (or any other Telegram Bots) on Vercel
*What is [Vercel](https://vercel.com/)?*
Fromn the official [Vercel](https://vercel.com/) website: 'Vercel lets teams deploy and run the user facing parts of their applications easily, separately from their backend.' 

Honestly, the 'Deploy telegram bot on Vercel(Python)' website blog by Chapi Menge (link: https://blog.chapimenge.com/blog/programming/deploying-on-vercel/) explains clearly step by step on how to deploy a Telegram Bot, built in Python on [Vercel](https://vercel.com/) (I believe that if you build the Telegram Bot using other programming languages such as JavaScript, the deployment process on [Vercel](https://vercel.com/) and the required code in the files will differ). There are various platforms where you can deploy your Telegram Bot, (e.g. [Heroku](https://heroku.com/), [Back4app](https://containers.back4app.com/), [Amazon Web Services](https://aws.amazon.com/) etc.) but deploying on [Vercel](https://vercel.com/) worked for me. Once deployed correctly, rather than getting a link for your website, the Telegram Bot should start to work as expected. You will also

**I did run into quite a few difficulties deploying the Telegram Bot on Vercel, which I spent a great deal of time trying to debug, even while following the website blog by Chapi Menge due to my lack of knowledge in deploying on [Vercel](https://vercel.com/), and that the website blog by Chapi Menge is not the clearest. Here are some of the background knowledge required to deploying on [Vercel](https://vercel.com/):**
- My confusion on what is a Webhook and what is Long Polling:
  - What is a Webhook?
    A webhook is a way for an application to send real-time data to another system when triggered by certain events. It only sends HTTP requests to the system when triggered by a (certain) event. (hence more efficient than Long Polling)

    What is Long Polling?
    Long Polling is a way for an application to send real-time data to another system by maintaining a constant connection to constantly check for updates between the application and the system. It constantly sends HTTP requests to the system. (hence less efficient than Long Polling)

    However, for [Vercel](https://vercel.com/), it only works with applications that uses Webhooks instead of Long Polling due to its architecture its just like that). And unfortunately, when I first built the Telegram Bot locally on my laptop (see the first iteration in the prototype folder?), I used Long Polling for my Telegram Bot instead, and hence caused my Telegram Bot to be unable to be deployed on [Vercel](https://vercel.com/), which the website blog by Chapi Menge did not warn very clearly and took me a great deal of time trying to debug. This is when I realised 

    For the case of deploying the Telegram Bot on [Vercel](https://vercel.com/) for this project,
    
    

  - Here is how a webhook works in the case of deploying this Telegram Bot on [Vercel](https://vercel.com/), 


Since originallly as taught in the telegram bot tutorials it uses long pollin gby default. So when deploying thee telegram bot in Vercel I need to use Webhooks instead. So I just use ChatGPT to help me convert my Telegram Bot using long pollin got use webhook sinsgtead directly (hence I technically have no idea how to convert to the webhook thing myself in the deployment process (using the python libraries FastAPI, Pydantic, os, etc.) (that you will see in the 'index.py' file), I only know how to do the long polling in telegram bot thing, which only works locally, but not in deployment (globally) 
      

So where is the actual file? Its in the index.py as webhook...

Here is the link of my 'itch.io' account of the username:, 'WindJammer6' - https://windjammer6.itch.io/.
Here is the link of this deployed 2D Unity game on 'itch.io' - https://windjammer6.itch.io/2d-unity-game-by-windjammer6

Source(s):
https://vercel.com/ (Vercel)
https://vercel.com/blog/what-is-vercel (Vercel Blog)
https://www.youtube.com/watch?v=UK7SEoiSB2c (GDTitans) (Youtube video labelled 'How To Build & Deploy Your Games With WebGL' by GDTitans)

