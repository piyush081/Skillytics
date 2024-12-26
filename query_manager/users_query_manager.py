from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from db_connection import SessionLocal
from schemas.users import User

class UserQryManager():


    def get_all_users():
        """
        Fetch all users from the database.
        :return: List of user dictionaries or an error message.
        """
        session = SessionLocal()
        try:
            users = session.query(User).all()
            return [{"id": user.id, "name": user.name, "email": user.email, "created_on": user.created_on} for user in users]
        except SQLAlchemyError as e:
            return {"error": str(e)}
        finally:
            session.close()

    def check_user(username:str ,email: str=None):

        session = SessionLocal()
        try:
            users = session.query(User).filter(User.name == username)

            if email:
                email_check=users.filter(User.email==email)
                users=email_check.all()
            else:
                users.all()
            return [
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "created_on": user.created_on,
                }
                for user in users
            ]
        except SQLAlchemyError as e:
            return {"error": str(e)}
        finally:
            session.close()

    def add_user(username: str, email: str=None, ip: str=None):
        
        db = SessionLocal()
        try:
            user = User(
                name=username,
                email=email,
                ip_address=ip
            )

            db.add(user)
            db.commit()

            return {"message": "User added successfully!"}
        except SQLAlchemyError as e:
            db.rollback()
            return {"error": str(e)}
        finally:
            db.close()