from aiogram.dispatcher.filters.state import State, StatesGroup

class Movies(StatesGroup):
    code = State()
    

class MoviesSearch(StatesGroup):
    waiting_for_query = State()
    down = State()



class Treyler(StatesGroup):
    treyler_title = State()
    treyler_send = State()
