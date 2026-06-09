from aiogram import F, Router# type: ignore
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto# type: ignore
from aiogram.filters import CommandStart, Command # type: ignore
from rolls import roll_deploy, roll_second
import asyncio


router = Router()

@router.message(CommandStart()) # ОБРАБОТКА КОМАНДЫ СТАРТ 
async def start(message: Message):
    with open('kenti.txt', 'r') as f:
        kent = f.read().split('\n')
    this_user = message.from_user.username
    if this_user in kent:
        await message.answer(f'ОООО Здарова {this_user}\nВводи команду!')
    else:
        await message.answer(f'Ты кто?')


@router.message(Command("roll_deploy")) 
async def deploy(message: Message):
    # await message.delete()
    image = await roll_deploy()
    await message.answer_photo(FSInputFile(image))


@router.message(Command("roll_deploy")) 
async def second(message: Message):
    
    media = await roll_second(None)
    
    # Отправляем альбом
    await message.answer_media_group(media=media)



if __name__ == "__main__":
    with open('kenti.txt', 'r', encoding='utf-8') as f:
        kent = f.read().split('\n')
    print(kent)
