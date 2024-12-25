import time
from aiogram import Bot
import logging


# Уведомление администраторам бота о том что Бот запущен

async def on_startup_notify(bot: Bot):
    logging.info('on_startup_notify')
    date_now = time.strftime("%Y-%m-%d", time.localtime())
    time_now = time.strftime("%H:%M:%S", time.localtime())
    try:
        text = (f"✅Бот запущен и готов к работе!✅\n"
                f"📅Дата: {date_now}\n"
                f"⏰Время: {time_now}")
        await bot.send_message(chat_id=843554518, text=text)
    except Exception as err:
        logging.exception(err)
