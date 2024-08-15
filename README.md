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
+ https://t.me/test_12171_bot (Telegram Bot named 'Telegram_Chatbot_integrated_with_Chatbase_GPT_model_API') 
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

4. Deployment Process of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database (or any other application) on Vercel  

<br>

## 1. Files required in the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database

<br>

## 2. Past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database
Telegram_bot.py is not required and is just merely for local running as long polling. (refer to the deployment process)

Wanted to

<br>

## 3. My learning journey of some of the required technology being used in this project that I was not familiar with
Due to my lack of knowledge in some of the required technology being used in the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, I had to first learn them, which includes:
- Building a Telegram Bot in Python (using the 'telegram.ext' (Python Framework) Telegram Bot API)
- Using Chatbase API (requires money)
- OpenAI API (but ended up not using it)

What is [Chatbase](https://www.chatbase.co/)?  
'Chatbase is an AI chatbot builder that allows companies and other users to create their own chatbot trained on their specific data, such as documentation or website content.'    
Source: https://www.techopedia.com/definition/chatbase (Techopedia)  

<br>

## 4. Deployment Process of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database (or any other application) on Vercel ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=vercel)
*What is [Vercel](https://vercel.com/)?*  
From the official [Vercel](https://vercel.com/) website: 'Vercel lets teams deploy and run the user facing parts of their applications easily, separately from their backend.' 

Honestly, the 'Deploy telegram bot on Vercel(Python)' website blog by Chapi Menge (link: https://blog.chapimenge.com/blog/programming/deploying-on-vercel/) explains clearly step by step on how to deploy a Telegram Bot, built in Python on [Vercel](https://vercel.com/) (I believe that if you build the Telegram Bot using other programming languages such as JavaScript, the deployment process on [Vercel](https://vercel.com/) and the required code in the files will differ). There are various platforms where you can deploy your Telegram Bot, (e.g. [Heroku](https://heroku.com/), [Back4app](https://containers.back4app.com/), [Amazon Web Services](https://aws.amazon.com/) etc.) but deploying on [Vercel](https://vercel.com/) worked for me. Once deployed correctly, rather than getting a link for your website, the Telegram Bot should start to work as expected. 

I chose Vercel also since its the only deployment platform that didnt require me to put in billing information, while the rest all need. Same for the firebase, which caused me to ultimately changed to it from MySQL server since basically all platforms I found to host my MYSQL server in the cloud required me to put billing information (I didnt want to spend moneyy) unfortunately, while only firebase didnt need

<br>

**I did run into quite a few difficulties deploying the Telegram Bot on Vercel, which I spent a great deal of time trying to debug, even while following the website blog by Chapi Menge due to my lack of knowledge in deploying on [Vercel](https://vercel.com/), and that the website blog by Chapi Menge is not the clearest. Here are some of the background knowledge and additional information that I found helpful to deploying on [Vercel](https://vercel.com/):**
- What is a Webhook and what is Long Polling? (that is mentioned in the website blog by Chapi Menge)
  - What is a Webhook?  
    A webhook is a way for an application to send real-time data to another system when triggered by certain events. It only sends HTTP requests to the system when triggered by a (certain) event. (hence more efficient than Long Polling)

    What is Long Polling?  
    Long Polling is a way for an application to send real-time data to another system by maintaining a constant connection to constantly check for updates between the application and the system. It constantly sends HTTP requests to the system. (hence less efficient than Long Polling)

    However, for [Vercel](https://vercel.com/), it only works with applications that uses Webhooks instead of Long Polling due to its architecture (its just like that). And unfortunately, when I first built the Telegram Bot locally on my laptop (see the first iteration in the prototype folder?), the code I used to build the Telegram Bot was using Long Polling instead. You can tell that the Telegram Bot is using Long Polling from the following code in the first iteration of the Telegram Bot:
    ```
    updater.start_polling()
    updater.idle()
    ```
    and hence caused my Telegram Bot to be unable to be deployed on [Vercel](https://vercel.com/), which the website blog by Chapi Menge did not warn very clearly and took me a great deal of time trying to debug. This is when I realised I need to change the code of the Telegram Bot to use Webhooks instead!

  - What is the 'index.py' file in the 'api' folder for? (that is mentioned in the website blog by Chapi Menge)  
    It was unfortunately not mentioned very clearly in the website blog by Chapi Menge, but 'index.py' (and the name has to be 'index.py' for some reason and not anything else) basically is supposed to hold the main code of the application, and the application must include code that allows it to handle Webhooks. I thought it was a little weird to put the main code of the application in the 'index.py' file in the 'api' folder... but it works for some reason.

    **IMPORTANT**  
    For this Telegram Bot, in order to get the Telegram Bot to use Webhooks instead of Long Polling, I simply just took reference from the provided 'index.py' file in the website blog by Chapi Menge, which used a sample Telegram Bot code built by Chapi Menge, and used [ChatGPT](https://chatgpt.com/) to adapt my first iteration of the Telegram Bot using Long Polling (with minor changes to my code, you can compare the 'index.py' file in this Github repository to the first iteration in the prototype folder file), to use Webhooks instead in order to deploy the Telegram Bot on [Vercel](https://vercel.com/). From what I observed, [ChatGPT](https://chatgpt.com/) used various other Python libraries that I am not familiar with, which are the 'FastAPI', 'pydantic', 'typing' and 'os' Python libraries that were not initially in my first iteration of the Telegram Bot to adapt it to use Webhooks instead of Long Polling.
    
  - According to the website blog by Chapi Menge, I needed to 'go to vercel and see the deployment is happening. After the deployment is finished, you can go to the Settings tab and click on Environment Variables. Add the 'TOKEN' variable and add the token of your bot.' What is this part talking about? (that is mentioned in the website blog by Chapi Menge)  
    The website blog by Chapi Menge is referring to adding the 'TOKEN' Environment variable and the corresponding Telegram Bot's token value/data/information to the application in [Vercel](https://vercel.com/). 

    Environment variables are key-value pairs that are stored outside the application's code and are used by the operating system and applications to configure behavior. These variables are accessible to the application at runtime and are typically used to store configuration settings and important information such as:
    - API keys
    - Database connection strings
    - Credentials (e.g. username/password)
    - Paths (e.g. file system locations)
    - Application modes (e.g. development, production)
   
    In this Telegram Bot, variables that are used as Environment variables include those containing the value/data/information of the Telegram Bot Token, Chatbase API key, Firebase Realtime Database URL, etc. You can see the Environment variables being used in the Telegram Bot's main code in the 'index.py' file here:
    ```python
    # Configuration for Chatbase, Telegram Bot and Firebase
    FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL')
    CHATBASE_API_URL = 'https://www.chatbase.co/api/v1/chat'
    CHATBASE_API_KEY = os.environ.get('CHATBASE_API_KEY')
    CHATBASE_CHATBOT_ID = os.environ.get('CHATBASE_CHATBOT_ID')
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')  # Make sure to set this in your environment variables
    ```
    What the website blog by Chapi Menge is saying is that we need to manually add the data for these Environment variables (since they should be stored outside of the application's code) in [Vercel](https://vercel.com/) like so:
    1. Go to the settings of the application in Telegram Bot's main code in the 'index.py' file, and click on 'Environment variables'. There is a text box titled 'Key' and another text box titiled 'Value'. The 'Key' represent the name of Environment variable and the 'Value' represent the value/data/information of the Environment variable.
![Screenshot 2024-08-16 002526](https://github.com/user-attachments/assets/b9bd2c59-25e4-43cd-b6d7-5ea6f084885f)

    2. Lets say we added the 'TOKEN' Environment variable into the text box titled 'Key' and the Telegram Bot's token value/data/information into the text box titled 'Value'. It should show the list of added Environment variables and their corresponding value/data/information below here. Notice that the exact same names of these Environment variables are used in the Telegram Bot's main code in the 'index.py' file (make sure the Environment variable name manually added in the application in [Vercel](https://vercel.com/) and the main code of the application are the same in order to use it properly!), this is because the Environment variables and their corresponding value/data/information that you manually added in [Vercel](https://vercel.com/) are indeed being read/extracted and used in the Telegram Bot's main code in the 'index.py' file
![Screenshot 2024-08-16 002547](https://github.com/user-attachments/assets/366a70eb-33c0-4719-aefb-67c342cfc8c1)

    Not super sure why the value/data/information of the Environment variables can't be manually inputted into the main code of the application, but needed to be separated from the main code of the application and be manually added into the application in [Vercel](https://vercel.com/)... but it works.
    
  - I got the error 'The Serverless Function has crashed' in [Vercel](https://vercel.com/). What does it mean and what do I do?  
    It means there is some issue with the main code of the application. You can check the 'Logs' of the application in [Vercel](https://vercel.com/) to see the full error.

    Due to my lack of knowledge in deploying applications in [Vercel](https://vercel.com/), I repeatedly copied the full error that showed in the 'Logs' of the application in [Vercel](https://vercel.com/), and asked [ChatGPT](https://chatgpt.com/) to tell me about the error and how to fix them, until I stopped getting errors and the application started to work.
  
  - What is this command 'curl 'https://api.telegram.org/bot<token>/setWebhook?url=https://telegram-bot.vercel.app/webhook' for? Where do I run it? (that is mentioned in the website blog by Chapi Menge)  
    The last thing that we need to do to deploy an application in [Vercel](https://vercel.com/) is to apparently run this command to 'set the Webhook' (idk what exactly this means, but you need to do this step in order to deploy an application in [Vercel](https://vercel.com/)):
    ```
    curl https://api.telegram.org/bot<token>/setWebhook?url=https://telegram-bot.vercel.app/webhook
    ```
    with '\<token>' replaced with the Telegram Bot token.
 
    However, since I am using Windows with Powershell in my VS code, this did not work for me as I had to go through the extra trouble of downloading the [curl](https://curl.se/download.html) software as well to run this command. So I used [ChatGPT](https://chatgpt.com/) to offer any alternative commands that works for Windows with Powershell in my VS code, in which it suggested I try this command, which works for me:
    ```
    $url = "https://api.telegram.org/bot<token>/setWebhook"
    $body = @{ url = "https://<your-vercel-app-url>/webhook" }
    Invoke-RestMethod -Method Post -Uri $url -Body $body
    ```
    with '\<token>' replaced with the Telegram Bot token and '\<your-vercel-app-url>' replaced with the URL of the application in [Vercel](https://vercel.com/).
 
    You can tell that the command works if it returns the following message:
    ```
    {"ok":true,"result":true,"description":"Webhook was set"}
    ```
    
    According to the website blog by Chapi Menge, you can run this command anywhere, including the terminal and VS code, but running it in VS code worked for me. 
      

Here is the link of my [Vercel](https://vercel.com/) account of the username: 'WindJammer6' - https://vercel.com/windjammer6s-projects.
Here is the link of this deployed Telegram Bot (named 'Telegram_Chatbot_integrated_with_Chatbase_GPT_model_API') using [Vercel](https://vercel.com/) - https://t.me/test_12171_bot

Source(s):
https://vercel.com/ (Vercel)
https://vercel.com/blog/what-is-vercel (Vercel Blog)
https://www.youtube.com/watch?v=UK7SEoiSB2c (GDTitans) (Youtube video labelled 'How To Build & Deploy Your Games With WebGL' by GDTitans)
https://chatgpt.com/ (ChatGPT)

