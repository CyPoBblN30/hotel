from database import get_db
from database.models import Booking


# добавление бронирования
def add_booking_db(user_id, room_id, start_date, end_date):
    db = next(get_db())
    new_booking = Booking(user_id=user_id, room_id=room_id, start_date=start_date, end_date=end_date)
    db.add(new_booking)
    db.commit()
    return True


# получение всех бронирований
def get_all_bookings_db():
    db = next(get_db())
    all_bookings = db.query(Booking).all()
    return all_bookings


# получение определённого бронирования
def get_exact_booking_db(booking_id):
    db = next(get_db())
    exact_booking = db.query(Booking).filter_by(id=booking_id).first()
    return exact_booking


# удаление определённого бронирования
def delete_booking_db(booking_id):
    db = next(get_db())
    delete_booking = db.query(Booking).filter_by(id=booking_id).first()
    db.delete(delete_booking)
    db.commit()
    return True


# изменение определённого параметра бронирования
def update_booking_db(booking_id, old, new):
    db = next(get_db())
    update_booking = db.query(Booking).filter_by(id=booking_id).first()
    if update_booking:
        if old == 'start_date':
            update_booking.start_date = new
        elif old == 'end_date':
            update_booking.end_date = new
        else:
            return False
        db.commit()
        return True
    return False