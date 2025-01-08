from fastapi import APIRouter
from database.roomservice import *
from api import result_message


room_router = APIRouter(prefix='/room', tags=['Номера отеля'])


@room_router.post('/add_room')
async def add_room(room_type: str, price: int, availability: int):
    result = add_room_db(room_type=room_type, price=price, availability=availability)
    return result_message(result)


@room_router.get('/get_all_rooms')
async def get_all_rooms():
    result = get_all_rooms_db()
    return result_message(result)


@room_router.get('/get_exact_room')
async def get_exact_room(room_id: int):
    result = get_exact_room_db(room_id=room_id)
    return result_message(result)


@room_router.put('/update_room')
async def update_room(room_id: int, old: str, new: str):
    result = update_room_db(room_id=room_id, old=old, new=new)
    return result_message(result)


@room_router.delete('/delete_room')
async def delete_room(room_id: int):
    result = delete_room_db(room_id=room_id)
    return result_message(result)