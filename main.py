from fastapi import FastAPI
from api.user_api.users import user_router
from api.room_api.rooms import room_router
from api.booking_api.bookings import booking_router
from database import Base, engine

app = FastAPI(docs_url='/')


Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(room_router)
app.include_router(booking_router)
