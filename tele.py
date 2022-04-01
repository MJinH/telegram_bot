import telepot
import logging
from module import command_list, get_weather, get_coin

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def bot_handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == "text":
        tele_message = msg["text"]
        if tele_message[0] == "/":
            command_type = tele_message.split(" ")
            if command_type[0] == "/list":
                try:
                    del command_type[0]
                    dir_path = "".join(command_type)
                    files_list = command_list(dir_path)
                    tele_bot.sendMessage(chat_id,files_list)
                except Exception as e:
                    tele_bot.sendMessage(chat_id,"/list error. The path should be /list [file or folder path]")
            if command_type[0] == "/weather":
                try:
                    del command_type[0]
                    location = "".join(command_type)
                    data = get_weather(location)
                    print(data)
                    str_data = ""
                    for v in data:
                        str_data += data[v]
                        str_data += "\r\n"
                    tele_bot.sendMessage(chat_id,str_data)
                except Exception as e:
                    tele_bot.sendMessage(chat_id,"/weather error. The command should be /weather [location].")
            if command_type[0] == "/coin":
                try:
                    del command_type[0]
                    coin = "".join(command_type)
                    data = get_coin(coin)
                    str_data = ""
                    for v in data:
                        str_data += data[v]
                        str_data += "\r\n"
                    tele_bot.sendMessage(chat_id,str_data)
                except Exception as e:
                    tele_bot.sendMessage(chat_id,"/coin error. The command should be /weather [coin].")
        
        else:
            tele_bot.sendMessage(chat_id,"Command needes to start with /")
        
        

'''
TELEGRAM_TOKE = "Your Token here"
'''
tele_bot = telepot.Bot(TELEGRAM_TOKE)
tele_bot.message_loop(bot_handler,run_forever=True)