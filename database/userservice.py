from database import get_db
from database.models import User


# добавление пользователя
def add_user_db(surname, name, phone_number):
    db = next(get_db())
    new_user = User(surname=surname, name=name, phone_number=phone_number)
    db.add(new_user)
    db.commit()
    return True


# получение всех пользователей
def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


# получение определённого пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    return exact_user


# удаление определённого пользователя
def delete_user_db(user_id):
    db = next(get_db())
    delete_user = db.query(User).filter_by(id=user_id).first()
    db.delete(delete_user)
    db.commit()
    return True


# изменение определённого параметра пользователя
def update_user_db(user_id, old, new):
    db = next(get_db())
    update_user = db.query(User).filter_by(id=user_id).first()
    if update_user:
        if old == 'surname':
            update_user.surname = new
        elif old == 'name':
            update_user.name = new
        elif old == 'phone_number':
            update_user.phone_number = new
        else:
            return False
        db.commit()
        return True
    return False