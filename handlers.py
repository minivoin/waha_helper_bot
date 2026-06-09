from aiogram import F, Router# type: ignore
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto# type: ignore
from aiogram.filters import CommandStart, Command # type: ignore
import asyncio


router = Router()

@router.message(CommandStart) # ОБРАБОТКА КОМАНДЫ СТАРТ 
async def start(message: Message):
    with open('kenti.txt', 'r') as f:
        kent = f.read().split('\n')
    print(message.from_user.usernam)



if __name__ == "__main__":
    with open('kenti.txt', 'r', encoding='utf-8') as f:
        kent = f.read().split('\n')
    print(kent)
