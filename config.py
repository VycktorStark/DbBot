#-*- coding: utf-8 -*-
# encoding: utf-8
#qpy:console
#qpy:2
import lang, platform, os

cihaz=platform.system()
if(cihaz=="Linux"):
    x="/sdcard/qpython/scripts/"
elif(cihaz=="Symbian"):
    x="/root/"
else:
    x="/root/"
ru = lambda text: text.decode('utf-8', 'ignore')
ur = lambda text: text.encode('utf-8', 'ignore')
name = '%s.txt' % lang.Info('config').get_info().replace(' ', '')
conf = '%s%s' % (os.getcwd(), name)
conf=x+conf

class Sets:

    def __init__(self):
        self.apiTokenBotMaster = ''
        self.apiTokenBotBeta= ''
        self.load()

    def load(self):
        try:
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)

        except:
            self.save()
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)

    def save(self):
        data = ''
        for name in self.__dict__.keys():
            line = name + ' = ' + repr(self.__dict__[name]) + '\r\n'
            data += line

        open(conf, 'wb').write(ur(data))
        del data
