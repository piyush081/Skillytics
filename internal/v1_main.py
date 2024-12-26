import re
import requests
from query_manager.users_query_manager import UserQryManager
from db_connection import engine
from schemas.users import User

engine=engine.connect()

class CoreUtilities():

    def get_all_users():
        
        user_details=UserQryManager.get_all_users()
        return user_details
    
    def get_user_details(username:str, email:str):

        pattern_username = r"^[a-zA-Z][a-zA-Z0-9_.@]*$"
        pattern_email = r"^[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

        if re.match(pattern_username, username):
            pass
        else:
            return "Input must start with an alphabet and only contain alphanumeric characters, '_', '.', '@', and no spaces."

        if email is not None:
            if re.match(pattern_email, email):
                print("Valid email")
            else:
                return "Invalid email format. Please provide a valid email address."
        
        existing_user=UserQryManager.check_user(username=username, email=email)
        print(existing_user)
        try:
            response = requests.get("https://api.ipify.org?format=json")
            ip=response.json().get("ip")
        except Exception as e:
            print(f"Error retrieving IP: {e}")
        if email is None and existing_user:
            return "This Username is Unavailable"
        elif existing_user:
            update_user=UserQryManager.add_user(username=username, email=email, ip=ip)
            print(update_user)
            return "Welcome Back"
        else:
            update_user=UserQryManager.add_user(username=username, email=email, ip=ip)
            print(update_user)
            return "Welcome"
        
    def store_skills(user_details:dict):

        try:

            add_skills=UserQryManager.add_user_skill(user_id=user_details.user_id, skill=user_details.skill_name, experience=user_details.experience_in_months)
            print(add_skills)

        except Exception as e:
            print(f"Error retrieving IP: {e}")
