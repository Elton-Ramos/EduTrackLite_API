from pydantic import BaseModel, ConfigDict

class CourseBase(BaseModel):
    title: str
    description: str
    is_open: bool = True


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)