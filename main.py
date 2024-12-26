from typing import Optional
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db_connection import engine
from internal.v1_main import CoreUtilities
from query_manager.users_query_manager import UserQryManager

app = FastAPI()

engine=engine.connect()

@app.get("/users")
async def fetch_user_details():
    try:
        user_details=CoreUtilities.get_all_users()
        return user_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")


@app.post("/enter_details/{username}")
async def user_details(username: str, email: Optional[str] = None):
    try:
        user_details = CoreUtilities.get_user_details(username=username, email=email)
        return user_details
    except Exception as e:
        raise e


