from aiogram import types, Router
from aiogram.filters import Command
from bot.handlers import command_handler

router = Router()

@router.message(Command('start'))
async def startCommand(message: types.Message) -> None: 
    await command_handler.startCommand(message)

@router.message(Command('help'))
async def helpCommand(message: types.Message) -> None: 
    await command_handler.helpCommand(message)

@router.message(Command('status'))
async def statusCommand(message: types.Message) -> None: 
    await command_handler.statusCommand(message)

# @dp.message(content_types=types.ContentTypes.TEXT)
# async def textCommand(message: types.Message) -> None: 
#     await command_handler.textCommand(message)