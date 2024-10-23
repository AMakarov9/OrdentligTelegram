import asyncio, os, logging, signal

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from bot.bot import router
load_dotenv(".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


async def main(): 
    dp.include_router(router)
    await dp.start_polling(bot)

def signal_handler(sig, frame): 
    def force_exit(): 
        print("Forcing stop of program")
        os.kill(os.getpid(), signal.SIGILL)
    force_exit()


if __name__ == '__main__': 
    logging.basicConfig(level=logging.INFO)
    signal.signal(signal.SIGINT, signal_handler)
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")