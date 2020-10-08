# Tutorial: https://blog.finxter.com/python-telegram-bot/

from datetime import date, timedelta
import telebot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import schedule
from threading import Thread
from time import sleep

updater = None

# Variavel que para a rotina
stop_rotina = False

################################## Comandos gerais do BOT ##################################

# Responde ao comando /help
# Envia informações sobre o BOT
def ajuda(update, context):
    message = "Olá, eu sou a Sexta-feira, sou feita para testes!"
    update.message.reply_text(message)

def HelloThere(update, context):
    update.message.reply_text("Olá chefe, como vai?")

# Thread que acorda a cada segundo e verifica se há alguma tarefa agendada
def schedule_checker():
    while True:
        #if stop_rotina: 
        #    break
        schedule.run_pending() # Executando todas as funções agendadas para o horário
        sleep(1)
        

def Iniciar(update, context):
    # Executará toda quinta as 12h
    # fazer as opções de dias
    schedule.every().hour.do(HelloThere, update, context)
    Thread(target=schedule_checker).start() 
    update.message.reply_text("Pode deixar chefe")

def PararRotina(update, context):
    stop_rotina = True
    update.message.reply_text("Ok, chefe")




################################## Controle do BOT ##################################

# Token do BOT do Telegram
TOKEN = "1305351200:AAHnlql7YK3TVRGZCLbgkyeh_lEY4ERfP6o"

# Função responsavel por inicializar o bot
def start_bot():
    global updater
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    # Definindo quais comandos o BOT irá ouvir
    dispatcher.add_handler(CommandHandler('start', Iniciar))
    dispatcher.add_handler(CommandHandler('help', ajuda))

    # Inicializando o bot
    updater.start_polling(poll_interval = 1.0,timeout=20) 
    # Bloqueia o script até que o programador mande um comando para derrubar a aplicação
    updater.idle()

start_bot()