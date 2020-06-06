from lang import textofcode
import random
class Plugin:
	def __init__(self, msg):
		self.msg = msg
		self.nomeuser = msg['from']['first_name']
		if ('last_name' in self.msg['from']): 
			self.nomeuser = f"{self.nomeuser} {msg['from']['last_name']}"
		if ('username' in self.msg['from']): 
			self.usernameuser = f"@{msg['from']['username']}"
		else:
			self.usernameuser = False
		self.iduser = msg['from']['id']
		self.text = str(msg['text'])
		self.bloco = str(self.text).split()
		self.cmd = self.bloco[0]
	def command(self):
		if (self.cmd ==  "/start"):
			return textofcode['start'].format(name=self.nomeuser)
		if (self.cmd == "/jokenpo"):
			return random.choice(["✌","👋","✊"])
		if self.cmd == "/id":
			if (self.usernameuser == False):
				resp=textofcode['idinfo'].format(username_='\n', name_=self.nomeuser, id_=self.iduser)
			else:
				resp=textofcode['idinfo'].format(username_=f'\nUsuario: {self.usernameuser}\n', name_=self.nomeuser, id_=self.iduser)
			return resp
		if ("/help" in self.bloco):
			if len(self.bloco) == 1:
				return textofcode['help']
			else:
				return self.__help()
	def __help(self):
		if (("1" == self.bloco[1]) or ('jokenpo' == self.bloco[1])):
			return textofcode['desc'].format(cmd="/jokenpo", desc=textofcode["jokenpo"])
		elif (('2' == self.bloco[1]) or ('id' == self.bloco[1])):
			return textofcode['desc'].format(cmd="/id", desc=textofcode['id'])
		else:
			return textofcode['notcmd']
