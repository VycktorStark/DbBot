#!/usr/bin/env python
#-*- coding: utf-8 -*-

import telepot,random, re, sys, time, datetime,json
from plugin import *
from bot import *
from config import *
from lang import *
from PythonColorize import *
ru = lambda text: text.decode('utf-8', 'ignore')
class Server:
    def about(self, title = ''):
        self.info = []
        self.info.append(colors.lg_red +'{tag}[ '.format(tag='=' * 9) + colors.nocolor + title + colors.lg_red + ' ]{tag}\n'.format(tag='=' * 9))
        self.info.append(colors.lg_cyan + 'Nome do Projeto: ' + colors.nocolor + lang('projectname').info())
        self.info.append(colors.lg_cyan + '\nVersao: ' + colors.nocolor + lang('version').info())
        self.info.append(colors.lg_cyan + '\nAutor: ' + colors.nocolor + lang('create').info())
        self.info.append(colors.lg_cyan + '\nContribuidores: \n' + colors.nocolor + lang('contribuidores').info())
        self.info.append(colors.lg_cyan + '\nGrupo de suporte: ' + colors.nocolor + lang('grupo').info())
        self.info.append(colors.lg_cyan + '\nSource code: ' + colors.nocolor + lang('source').info() + "\n\n")
        return ru("".join(self.info))

    def show(self):
        sys.stderr.write(self.about('Sobre'))
        time.sleep(0)

if __name__ == '__main__':
  api.message_loop(handle)
  Server().show()    
print(colors.lg_red + "[" + hora + "] " + colors.lg_cyan + bot_name + " foi iniciado")
api.sendMessage(Chatsuporte, lang('init').pt_br().format(bot_name, bot_username, bot_id, data, hora), "HTML")
while 1:
    time.sleep(10)
