class UserState: 
    _user_state : dict[int, str] = {}

    @classmethod
    def getState(cls, chat_id: int) -> str: 
        return cls._user_state.get(chat_id, '')
    
    @classmethod
    def updateState(cls, chat_id: int, state: str) -> None: 
        cls._user_state[chat_id] = state
    
    @classmethod
    def delState(cls, chat_id: int) -> None: 
        del cls._user_state[chat_id]
