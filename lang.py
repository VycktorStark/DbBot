#-*- coding: utf-8 -*-
# encoding: utf-8
class Info:
    desc = "📖 <b>Ajuda para o comando:</b> <code>{}</code>\n\n{desc}"
    exemplo = "\n<b>____________</b>\nExemplo:\n"
    descSenha = "Para que seja gerada uma sugestão de senha" + exemplo + " <code>/senha 8</code> - gerar senha com 8 digitos\n<code>/senha 16</code> - gerar senha com 16 digitos"
    descHora = "Para informar a hora atual do bot."
    descDados = "Para girar o dado aleatoricamente e informar um resultado."
    descID = "Para o bot retorna algumas informações sobre você."
    descVersion = "Para o bot retorna algumas informações sobre ele."
    def __init__(self, get):
        self.get = get
    def lang(self):
        if self.get.lower() ==  "start":
            return "Olá, <b>{nome}</b>!\nEu sou um bot simples ainda estou aprendendo. <b>O que posso fazer para você no momento?</b>\n\n- Envie /ajuda agora mesmo para para saber!"
        if self.get.lower() ==  "init":
            return "Qual projeto deseja iniciar?\n1 - Bot Master\n2 - Bot Beta"
        if self.get.lower() ==  "info_id":
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
            return "📖 <b>Lista de Comandos:</b>\n <code>1</code> - dado\n <code>2</code> - hora\n <code>3</code> - id\n <code>4</code> - senha\n <code>5</code> - versão\n<b>________________</b>\nℹ️ Envie <code>/ajuda [</code><b>nome</b><code>/</code><b>número</b><code>]</code> para saber como utilizar tal comando, ou clique sobre o atalho destacado."

    def get_info(self):
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
            return 'Adilson Cavalcanti - @Player4NoobWinner\nTiago Danin - @TiagoEDGE'
        if self.get.lower() == 'source':
            return 'https://github.com/VycktorStark/QPython-Telegram-bot-api'
