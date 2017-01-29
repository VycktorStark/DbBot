import telepot
from config import *
TokenBot = "token"
Chatsuporte = "-1001097459691"
api = telepot.Bot(TokenBot)
bot = api.getMe()
bot_name = bot['first_name']
bot_username = '@' + bot['username']
bot_id = bot['id']
