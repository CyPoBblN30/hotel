from database import Base
from sqlalchemy import (Column, Integer, String, DateTime, ForeignKey)
from datetime import datetime



### создание моделей

# гости отеля
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


# номера
class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_type = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    availability = Column(Integer, nullable=False)    # Количество доступных номеров


# бронирования
class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    start_date = Column(DateTime, default=datetime.now())
    end_date = Column(String, nullable=True)



