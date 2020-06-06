#!/usr/bin/env python
#-*- coding: utf-8 -*-
import telepot, os, random, time
Chatsuporte, api = 438131290, telepot.Bot(os.environ['TOKEN'])
bot = api.getMe()
bot_name, bot_username, bot_id = bot['first_name'], f"@{bot['username']}", bot['id']
def handle(msg):
	from plugin import Plugin
	cmd = None
	content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
	if (str(content_type) is 'text') and (str(chat_type) == "private"):
		if ('entities' in msg):
			if ('bot_command' == msg['entities'][0]['type']):
				try:
					cmd = Plugin(msg).command()
				except Exception as error:
					print(error)
				finally:
					if (not cmd is None):
						api.sendMessage(chat_id, cmd, reply_to_message_id=msg_id, parse_mode="HTML")
if __name__ == '__main__':
	from lang import textofcode
	api.message_loop(handle)
	print(f"{bot_name} was started")
	api.sendMessage(Chatsuporte, textofcode['init'].format(bot_name, bot_username, bot_id), "HTML")
	while True:
		time.sleep(10)