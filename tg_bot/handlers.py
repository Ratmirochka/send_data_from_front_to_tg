from aiogram import Router, types
from aiogram.filters import Command
from settings import settings

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Бот запущен и готов получать сообщения с сайта")