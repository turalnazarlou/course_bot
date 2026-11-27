
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import ADMIN_IDS

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Welcome to our Academy!\n\n"
        "Use /courses to explore our courses."
    )


@dp.message(Command("courses"))
async def courses_command(message: Message):
    await message.answer(
        "Our courses will appear here soon!"
    )


@dp.message(Command("admin"))
async def admin_command(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("You are not authorized.")
        return

    await message.answer(
        "Welcome to the Admin Panel!"
    )
