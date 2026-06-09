from aiogram import F, Router# type: ignore
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto# type: ignore
from aiogram.filters import CommandStart, Command # type: ignore
from rolls import roll_deploy, roll_second, roll_rule
import asyncio


router = Router()

@router.message(CommandStart()) # ОБРАБОТКА КОМАНДЫ СТАРТ 
async def start(message: Message):
    await message.answer('Привет я бот для раздачи говна')


@router.message(Command("roll_deploy")) 
async def deploy(message: Message):
    image = await roll_deploy()
    await message.answer_photo(FSInputFile(image))


@router.message(Command("roll_second")) 
async def second(message: Message):
    image = await roll_second()
    await message.answer_photo(FSInputFile(image))


@router.message(Command("roll_rule")) 
async def rule(message: Message):
    image = await roll_rule()
    await message.answer_photo(FSInputFile(image))


