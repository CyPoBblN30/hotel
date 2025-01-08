from fastapi import APIRouter
from database.bookingservice import *
from api import result_message


booking_router = APIRouter(prefix='/booking', tags=['Бронирования номеров отеля'])


@booking_router.post('/add_booking')
async def add_booking(user_id: int, room_id: int, start_date: str, end_date: str):
    result = add_booking_db(user_id=user_id, room_id=room_id, start_date=start_date, end_date=end_date)
    return result_message(result)


@booking_router.get('/get_all_bookings')
async def get_all_bookings():
    result = get_all_bookings_db()
    return result_message(result)


@booking_router.get('/get_exact_booking')
async def get_exact_booking(booking_id: int):
    result = get_exact_booking_db(booking_id=booking_id)
    return result_message(result)


@booking_router.put('/update_booking')
async def update_booking(booking_id: int, old: str, new: str):
    result = update_booking_db(booking_id=booking_id, old=old, new=new)
    return result_message(result)


@booking_router.delete('/delete_booking')
async def delete_booking(booking_id: int):
    result = delete_booking_db(booking_id=booking_id)
    return result_message(result)