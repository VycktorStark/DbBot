#-*- coding: utf-8 -*-
# encoding: utf-8
ptdesc = "📖 <b>Ajuda para o comando:</b> <code>{}</code>\n\n{desc}"
ptexemplo = "\n<b>____________</b>\nExemplo:\n"
ptdescSenha = "Para que seja gerada uma sugestão de senha" + ptexemplo + " <code>/senha 8</code> - gerar senha com 8 digitos\n<code>/senha 16</code> - gerar senha com 16 digitos"
ptdescHora = "Para informar a hora atual do bot."
ptdescDados = "Para girar o dado aleatoricamente e informar um resultado."
ptdescID = "Para o bot retorna algumas informações sobre você."
ptdescVersion = "Para o bot retorna algumas informações sobre ele." 
class lang:
    def __init__(self, get):
        self.get = get
    def pt_br(self): 
        if self.get.lower() ==  "start":
            return "Olá, <b>{nome}</b>!\nEu sou um bot simples ainda estou aprendendo. <b>O que posso fazer para você no momento?</b>\n\n- Envie /ajuda agora mesmo para para saber!"
        if self.get.lower() ==  "init":
            return "<b>{} iniciado!\n______________\n</b>🤖 | <b>Username:</b> {}\n🖥 | <b>ID:</b> <code>{}</code>\n<b>______________\n📆 Data de conexão:</b> <code>{}</code>\n⌚️ <b>Hora da conexão:</b> <code>{}</code>"
        if self.get.lower() ==  "id_user":
            return "Nome: <b>{}</b>\nUsuário: {}\nID: <code>{}</code>"
        if self.get.lower() ==  "info":
            return '<b>Nome do Projeto:</b> {}\n<b>Autor:</b> {}\n<b>Versão:</b> <code>{}</code>\n<b>Contribuidores:</b> \n{}\n👥<b>Grupo de suporte:</b> <a href="{}">@DesenvolvimentoDeBots</a>\n💻 <a href="{}">Source code</a>'
        if self.get.lower() ==  "dados":
            return "O Dado parou no número: 🎲 <code>{}</code>"
        if self.get.lower() ==  "senha":
            return "Senha gerada: \n{}"
        if self.get.lower() ==  "hora":
            return "Pelo meu relógio agora são {}"
        if self.get.lower() ==  "ajuda":
            return "📖 <b>Lista de Comandos:</b>\n <code>1</code> - dado\n <code>2</code> - hora\n <code>3</code> - id\n <code>4</code> - senha\n <code>5</code> - info\n<b>________________</b>\nℹ️ Envie <code>/ajuda [</code><b>nome</b><code>/</code><b>número</b><code>]</code> para saber como utilizar tal comando, ou clique sobre o atalho destacado."

    def info(self):
        if self.get.lower() == 'config':
            return 'config'
        if self.get.lower() == 'grupo':
            return 'https://telegram.me/DesenvolvimentoDeBots'
        if self.get.lower() == 'version':
            return '1.0'
        if self.get.lower() == 'create':
            return 'Vycktor Stark'
        if self.get.lower() == 'projectname':
            return 'QPython-Telegram-bot-api'
        if self.get.lower() == 'contribuidores':
            return 'Adilson Cavalcante - @Player4NoobWinner\nTiago Danin - @TiagoEDGE'
        if self.get.lower() == 'source':
            return 'https://github.com/VycktorStark/QPython-Telegram-bot-api'
