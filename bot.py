from aiogram import Bot, Dispatcher# type: ignore
from handlers import router
import asyncio


async def main():
    bot = Bot(token='8774495189:AAH5gQ6pHPS51WEi9MtwTcXm6bQBSBqlnOs') ## ТОКИН БОТА
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print('БОТ РАБОТАЕТ')
        asyncio.run(main())
    except KeyboardInterrupt():
        print('БОТ ВЫКЛЮЧЕН')    

