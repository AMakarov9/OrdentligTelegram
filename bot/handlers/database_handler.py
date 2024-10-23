from supabase import create_client
import os
from dotenv import load_dotenv
from aiogram import types

class Database: 
    
    load_dotenv("navet/.env")
    
    _SUPABASE_URL = os.getenv("SUPABASE_URL")
    _SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    # print(_SUPABASE_URL, _SUPABASE_KEY)

    
    _supabase = create_client(_SUPABASE_URL, _SUPABASE_KEY)
    _table_name = 'test'

    _current_number = 0
    _user_limit = 20



    @classmethod 
    async def add_user(cls, message: types.Message) -> None: 
        print("Adding user")
        print(message.chat.id, message.chat.first_name)
        cls._supabase.table(cls._table_name).insert({'chat_id': message.chat.id, 'first_name': message.chat.first_name}).execute()
        cls._current_number += 1

   
    @classmethod
    async def check_user(cls, message: types.Message) -> bool: 

        print("Checking user")
        if cls._current_number >= cls._user_limit: 
            print("User limit reached")
            return False

        response = cls._supabase.table(cls._table_name).select('chat_id').eq('chat_id', str(message.chat.id)).execute()
        if response == []: 
            return False
        return True
    

    @classmethod
    async def del_user(cls, message: types.Message) -> None: 
        response = cls._supabase.table(cls._table_name).delete().eq('chat_id', str(message.chat.id)).execute()
        print("User deleted")




   
