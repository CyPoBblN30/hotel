from database import get_db
from database.models import Room


# добавление номера
def add_room_db(room_type, price, availability=50):
    db = next(get_db())
    new_room = Room(room_type=room_type, price=price, availability=availability)
    db.add(new_room)
    db.commit()
    return True


# получение всех номеров
def get_all_rooms_db():
    db = next(get_db())
    all_rooms = db.query(Room).all()
    return all_rooms


# получение определённого номера
def get_exact_room_db(room_id):
    db = next(get_db())
    exact_room = db.query(Room).filter_by(id=room_id).first()
    return exact_room


# удаление определённого номера
def delete_room_db(room_id):
    db = next(get_db())
    delete_room = db.query(Room).filter_by(id=room_id).first()
    db.delete(delete_room)
    db.commit()
    return True


# изменение определённого параметра номера
def update_room_db(room_id, old, new):
    db = next(get_db())
    update_room = db.query(Room).filter_by(id=room_id).first()
    if update_room:
        if old == 'room_type':
            update_room.room_type = new
        elif old == 'price':
            update_room.price = new
        elif old == 'availability':
            update_room.availability = new
        else:
            return False
        db.commit()
        return True
    return False