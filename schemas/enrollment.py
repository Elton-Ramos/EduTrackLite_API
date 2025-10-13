from pydantic import BaseModel, ConfigDict
from datetime import date

class EnrollmentBase(BaseModel):
    user_id: int
    course_id: int
    enrolled_date: date | None = None
    completed: bool = False


class EnrollmentCreate(EnrollmentBase):
    pass


class Enrollment(EnrollmentBase):
    id: int
    
model_config = ConfigDict(from_attributes=True)