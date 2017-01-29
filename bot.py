#-*- coding: utf-8 -*-
# encoding: utf-8
import telepot, lang, plugin, random, re
from config import *
from nltk.chat.iesha import iesha_chatbot
from PythonColorize import *
from plugin import *
is_chatting = True
sudo = 186513800
def handle(msg):
  global is_chatting
  content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
  nome_user = msg['from']['first_name']
  if 'last_name' in msg['from']: nome_user = nome_user + " " + msg['from']['last_name']
  username_user = "@" + msg['from']['username']
  id_user = msg['from']['id']
  if content_type == 'text':
    texto = msg['text'].split()
    input_texto  = " ".join(texto[1:])
    cmd = plugin(texto[0]).cmd()
    input_cmd = plugin(input_texto).help()
    print(colors.lg_red + "[{}] {} Enviou uma nova Mensagem de um {} (ID: {} )".format(hora, colors.nocolor +   msg['from']['first_name'], chat_type, colors.lg_red + str(chat_id) + colors.nocolor))
    print(colors.lg_blue + 'Mensagem Recebida: ' + colors.nocolor + msg['text'])
    if texto[0] == '/start':
      if id_user != sudo:
         if is_chatting == False:
            cmd = "BOT PARADO"
         else:
              api.sendMessage(chat_id, cmd.format(nome=nome_user), "HTML")
      else:
         is_chatting = True
         cmd = "BOT LIGADO"
         api.sendMessage(chat_id, cmd, "HTML")
    elif texto[0] == '/stop':
      if id_user != sudo:
         cmd = "Ei, você não manda em mim!"
         api.sendMessage(chat_id, cmd)
      else:
         is_chatting = False
         cmd ='BOT DESLIGADO'
         api.sendMessage(chat_id, cmd)
    elif msg['text'].startswith('yu ') and is_chatting == True:
       api.sendMessage(chat_id, iesha_chatbot.respond( msg['text'] ))
    elif cmd:
     if id_user == sudo or is_chatting == True:
        if texto[0] == "/senha":
           if input_texto != "16":
               api.sendMessage(chat_id, cmd.format(random.randint(00000000,99999999)))
           if input_texto == "16":
                api.sendMessage(chat_id, cmd.format(random.randint(0000000000000000,9999999999999999))) ##Fix -- Crédito ao @Player4NoobWinner
        elif texto[0] == '/id':
              api.sendMessage(chat_id, cmd.format(nome_user, username_user,  str(id_user)) , "HTML")
        elif texto[0] == "/ajuda":
              if len(texto) < 2:
                api.sendMessage(chat_id, cmd, 'HTML', reply_to_message_id=msg_id)
              elif input_cmd:
                   api.sendMessage(chat_id, input_cmd, 'HTML', reply_to_message_id=msg_id)
        else:
              api.sendMessage(chat_id, cmd, "HTML", reply_to_message_id=msg_id)

  if cmd or input_cmd:
        retorno = cmd or input_texto
        clean = re.compile('<[^<>]*>') ## REMOVING HTML
        retorno = re.sub(clean, "", retorno)
        print(colors.lg_green + "Mensagem Enviada: " + colors.nocolor+ retorno)
  return
