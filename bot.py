import asyncio
import os 
from aiogram import Bot, Dispatcher  # type: ignore
from handlers import router
from aiohttp import web  

PORT = int(os.getenv("PORT", 8080))


async def handle_ping(request):
    return web.Response(text="Бот работает!", status=200)


async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()


async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN", "Сюда токен бота"))
    dp = Dispatcher()

    dp.include_router(router)

    asyncio.create_task(start_web_server())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("БОТ РАБОТАЕТ")
        asyncio.run(main())
    except KeyboardInterrupt: 
        print("БОТ ВЫКЛЮЧЕН")
