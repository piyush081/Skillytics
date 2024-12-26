from pydantic import BaseModel, Field

class UserSkills(BaseModel):

    user_id: int
    skill_name: str
    experience_in_months: int

