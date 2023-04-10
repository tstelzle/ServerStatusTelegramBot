import asyncio
import configparser

from telegram import Bot

CONFIG = configparser.ConfigParser()
FILE = "/proc/mdstat"


async def read_mdstat():
    string_output = "MDSTAT: \n"
    with open(FILE, 'r') as f:
        for line in f:
            string_output += line

    await send_message(string_output)


async def send_message(message):
    bot = Bot(token=read_config_str("Telegram", "botToken"))
    try:
        response = await bot.send_message(chat_id=read_config_str("Telegram", "chatId"), text=message)
        print(response)
        return True
    except Exception as e:
        print(e)
        return False


def read_config_str(section: str, config_property: str) -> str:
    CONFIG.read("config.ini")
    return CONFIG.get(section, config_property)


if __name__ == '__main__':
    asyncio.run(read_mdstat())
