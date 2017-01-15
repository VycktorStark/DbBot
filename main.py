#!/usr/bin/env python
#-*- coding: utf-8 -*-
# encoding: utf-8
#qpy:console
#qpy:2
import sys, telepot, time, random, datetime, lang, androidhelper, threading, lang, config
from PythonColorize import *
ru = lambda text: text.decode('utf-8', 'ignore')
uptime = datetime.datetime.today()
hora = uptime.strftime("%H:%M:%S")
data = uptime.strftime("%d/%m/%Y")
droid = androidhelper.Android()
Nomebot = " ...."
response = droid.dialogGetInput("Iniciando bot", "Qual projeto deseja iniciar?\n1 - Bot Master\n2 - Bot Beta")
bot = response.result
if bot == "master" or bot == "1" or bot == "Master":
              bot = telepot.Bot(config.Sets().apiTokenBotMaster)
              Nomebot = 'Master'
elif bot == "beta" or bot == "2" or bot == "Beta":
              bot = telepot.Bot(config.Sets().apiTokenBotBeta)
              Nomebot = 'Beta'
else:print(colors.lg_red + "ERRO!!!"); time.sleep(500)

class Server:
    def about(self, title = ''):
        self.info = []
        self.info.append(colors.lg_red +'{tag}[ '.format(tag='=' * 9) + colors.nocolor + title + colors.lg_red + ' ]{tag}\n'.format(tag='=' * 9))
        self.info.append(colors.lg_cyan + 'Nome do Projeto: ' + colors.nocolor + lang.Info('projectname').get_info() )
        self.info.append(colors.lg_cyan + '\nVersao: ' + colors.nocolor + lang.Info('version').get_info())
        self.info.append(colors.lg_cyan + '\nAutor: ' + colors.nocolor + lang.Info('create').get_info())
        self.info.append(colors.lg_cyan + '\nContribuidores: \n' + colors.nocolor + lang.Info('contribuidores').get_info())
        self.info.append(colors.lg_cyan + '\nGrupo de suporte: ' + colors.nocolor + lang.Info('grupo').get_info())
        self.info.append(colors.lg_cyan + '\nSource code: ' + colors.nocolor + lang.Info('source').get_info() + "\n\n")
        return ru("".join(self.info))

    def show(self):
        sys.stderr.write(self.about('Sobre'))
        time.sleep(0)
        print(colors.lg_red + "[" + hora + "] " + colors.lg_cyan + str(Nomebot) + " iniciado")

def handle(msg):
  content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
  nome_user = msg['from']['first_name']
  if 'last_name' in msg['from']: nome_user = nome_user + " " + msg['from']['last_name']
  username_user = "@" + msg['from']['username']
  id_user = msg['from']['id']
  if content_type == 'text':
    texto = msg['text'].split()
    input_texto  = " ".join(texto[1:])
    print(colors.lg_red + "[ " + hora + " ] " + colors.lg_blue + nome_user +" Enviou uma nova Mensagem" + colors.nocolor)
    print("Enviada de um " + chat_type + " (ID:" + colors.lg_red + str(chat_id) + colors.nocolor + ")")
    print(colors.lg_blue + 'Mensagem: ' + colors.nocolor + msg['text'])
    if texto[0] == '/senha': ##Fix -- Crédito ao @Player4NoobWinner
        if not len(texto) == "16" : ##Fix -- Crédito ao @Player4NoobWinner
            bot.sendMessage(chat_id, lang.Info('senha').lang().format(random.randint(len(texto) ,99999999))) ##Fix -- Crédito ao @Player4NoobWinner
            return ##Fix -- Crédito ao @Player4NoobWinner
    if input_texto == "16": ##Fix -- Crédito ao @Player4NoobWinner
            bot.sendMessage(chat_id, lang.Info('senha').lang().format(random.randint(0000000000000000,9999999999999999))) ##Fix -- Crédito ao @Player4NoobWinner
    if texto[0] == '/ajuda':
        if len(texto) < 2:
            bot.sendMessage(chat_id, lang.Info('ajuda').lang(), 'HTML', reply_to_message_id=msg_id)
            return
    if input_texto == 'dado' or input_texto == "1":
            bot.sendMessage(chat_id, lang.Info.desc.format("Dado", desc=lang.Info.descDados), 'HTML')
    elif input_texto == 'hora' or input_texto == "2":
            bot.sendMessage(chat_id, lang.Info.desc.format("Hora", desc=lang.Info.descHora), 'HTML')
    elif input_texto == 'id' or input_texto == "3":
            bot.sendMessage(chat_id, lang.Info.desc.format("Id", desc=lang.Info.descID), 'HTML')
    elif input_texto == 'senha' or input_texto == "4":
            bot.sendMessage(chat_id, lang.Info.desc.format("Senha", desc=lang.Info.descSenha), 'HTML')
    elif input_texto == 'versão' or input_texto == "5":
        bot.sendMessage(chat_id, lang.Info.desc.format("Versão", desc=lang.Info.descVersion), 'HTML')
    if texto[0] == '/start':
        bot.sendMessage(chat_id, lang.Info('start').lang().format(nome=nome_user), "HTML")
    elif texto[0] == '/dados': ##Fix -- Crédito ao @Player4NoobWinner
        bot.sendMessage(chat_id, lang.Info('dados').lang().format(random.randint(1,9)), "HTML") ##Fix -- Crédito ao @Player4NoobWinner
    elif texto[0] == '/jokenpo': ##Fix -- Crédito ao @Player4NoobWinner
        bot.sendMessage(chat_id, random.choice(["✌","👋","✊"]), "HTML") ##Fix -- Crédito ao @Player4NoobWinner
    elif texto[0] == '/hora':
        bot.sendMessage(chat_id, lang.Info('hora').lang().format(hora))
    elif texto[0] == '/id':
        bot.sendMessage(chat_id, lang.Info('info_id').lang().format(nome_user, username_user,  str(id_user)), "HTML")
    elif texto[0] == '/info':
        bot.sendMessage(chat_id, lang.Info('info').lang().format(lang.Info('projectname').get_info(), lang.Info('create').get_info(),  str(lang.Info('version').get_info()), lang.Info('contribuidores').get_info(), lang.Info('grupo').get_info(), lang.Info('source').get_info()), "HTML")
  return ##FixBug -- Crédito ao @Tiagodanin


if __name__ == '__main__':
  Server().show()
time.sleep(2)
bot.message_loop(handle)
while 1:
    time.sleep(10)
