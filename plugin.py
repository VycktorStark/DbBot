#-*- coding: utf-8 -*-
# encoding: utf-8
from lang import *
from config import *
import random, datetime
uptime = datetime.datetime.today()
hora = uptime.strftime("%H:%M:%S")
data = uptime.strftime("%d/%m/%Y")
class plugin:
    def __init__(self, get):
        self.get = get
    def cmd(self):
        if self.get.lower() ==  "/start":
              return lang('start').pt_br()
        if self.get.lower() == "/dados":
               return lang('dados').pt_br().format(random.randint(1,9))
        if self.get.lower() == "/hora":
               return lang('hora').pt_br().format(hora)
        if self.get.lower() == "/info" or self.get.lower() == "/version":
               return lang('info').pt_br().format(lang('projectname').info(), lang('create').info(),  str(lang('version').info()), lang('contribuidores').info(), lang('grupo').info(), lang('source').info())
        if self.get.lower() == "/jokenpo":
               return random.choice(["✌","👋","✊"])
        if self.get.lower() ==  "/senha":
            return lang('senha').pt_br()
        if self.get.lower() == "/id":
               return lang('id_user').pt_br()
        if self.get.lower() == "/ajuda":
            return lang('ajuda').pt_br()
    def help(self):
        if self.get.lower() == "dado" or self.get.lower() == "1" :
               return ptdesc.format("/dados", desc=ptdescDados)
        if self.get.lower() == 'hora' or self.get.lower() == "2":
                return ptdesc.format("/hora", desc=ptdescHora)
        if self.get.lower() == 'id' or self.get.lower() == "3":
                return ptdesc.format("/id", desc=ptdescID)
        if self.get.lower() == 'senha' or self.get.lower() == "4":
                return ptdesc.format("/senha", desc=ptdescSenha)
        if self.get.lower() == 'info' or self.get.lower() == "5":
                return ptdesc.format("/info", desc=ptdescVersion)
