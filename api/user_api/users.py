from fastapi import APIRouter
from database.userservice import *
from api import result_message


user_router = APIRouter(prefix='/user', tags=['Гости отеля'])


@user_router.post('/add_user')
async def add_user(surname: str, name: str, phone_number: str):
    result = add_user_db(surname=surname, name=name, phone_number=phone_number)
    return result_message(result)


@user_router.get('/get_all_users')
async def get_all_users():
    result = get_all_users_db()
    return result_message(result)


@user_router.get('/get_exact_user')
async def get_exact_user(user_id: int):
    result = get_exact_user_db(user_id=user_id)
    return result_message(result)


@user_router.put('/update_user')
async def update_user(user_id: int, old: str, new: str):
    result = update_user_db(user_id=user_id, old=old, new=new)
    return result_message(result)


@user_router.delete('/delete_user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id=user_id)
    return result_message(result)

