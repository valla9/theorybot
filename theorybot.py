import telebot
import os
import modules.scales as scales

clients_scalegame = {}
def send_scale(id):
    clients_scalegame[id] = scales.get_scale_from_name_and_key()
    bot.send_message(id, clients_scalegame[id])
# create bot with imported token
# BOT_TOKEN is imported from the system environment variables
# TODO: change bot token variable name to GP_BOT_TOKEN
BOT_TOKEN = os.environ.get('BOT_TOKEN_THEORYBOT')
bot = telebot.TeleBot(BOT_TOKEN)
# [LEGACY] send welcome message 
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hey :)")

# start scale guessing game    
@bot.message_handler(commands=['scale'])
# starts a "chat thread" with user id
def handle_scale_game(message):
    send_scale(message.chat.id)

# end every game
@bot.message_handler(commands=['endgame'])
# starts a "chat thread" with user id
def handle_scale_game(message):
    chat_id = message.chat.id
    if chat_id in clients_scalegame:
        del clients_scalegame[chat_id]
    

# handle singe message without command
@bot.message_handler()
def hangle_message(message):
    # message id definition
    chat_id = message.chat.id
    # check if the message is for scale-guessing game
    if chat_id in clients_scalegame:
        if message.text == clients_scalegame[chat_id][1]:
            bot.send_message(chat_id, "Das ist richtig!")
            bot.send_message(chat_id, "Nächste Tonleiter:")
            send_scale(chat_id)
        else:
            bot.send_message(chat_id, "Das ist leider falsch... Rate nochmal!")
        

bot.infinity_polling()