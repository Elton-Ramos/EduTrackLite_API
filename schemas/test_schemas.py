from schemas.user import UserCreate
from schemas.course import CourseCreate
from schemas.enrollment import EnrollmentCreate
from datetime import date

user = UserCreate(name="Alice", email="alice@example.com")
course = CourseCreate(title="Math 101", description="Intro to Math")
enrollment = EnrollmentCreate(user_id=1, course_id=1)
print(user.model_dump())
print(course.model_dump())
print(enrollment.model_dump())