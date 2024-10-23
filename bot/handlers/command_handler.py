from aiogram import types
# import bot.temp_data.user_state as UserState
# import bot.handlers.database_handler as Database
from bot.temp_data.user_state import UserState
from bot.handlers.database_handler import Database

async def startCommand(message: types.Message) -> None: 
    UserState.updateState(message.chat.id, 'start')
    
    existing_user = await Database.check_user(message)

    if not existing_user: 
        await Database.add_user(message)
        await message.answer(
            text = 'Du har blitt lagt til som bruker'
        )
    
    else:
        await message.answer(
            text = 'Du er allerede registrert'
        )
        
async def helpCommand(message: types.Message) -> None:
    pass

async def statusCommand(message: types.Message) -> None:
    pass

async def textCommand(message: types.Message):
    state = UserState.getState(message.chat.id)

    if state == '':
        pass


async def varsleCommand(message: types.Message):
    pass

