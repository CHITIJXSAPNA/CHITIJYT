#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25318125"))
API_HASH = environ.get("API_HASH", "b29fb6a928e8b8a3308f8c2d3ba9cfb0")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7764674199"))
CREDIT = "𝄟⃝‌🐬𝑳𝑼𝑪𝑰𝑭𝑬𝑹🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '7764674199').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
