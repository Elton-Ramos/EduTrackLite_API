from schemas.user import User, UserCreate
from schemas.course import Course, CourseCreate
from schemas.enrollment import Enrollment, EnrollmentCreate

# Simulated in-memory “database”
users_db: list[User] = []
courses_db: list[Course] = []
enrollments_db: list[Enrollment] = []


# ---------- USER SERVICES ----------
def create_user(user: UserCreate) -> User:
    new_id = len(users_db) + 1
    user_data = User(id=new_id, **user.model_dump())   # model_dump = Pydantic v2 syntax
    users_db.append(user_data)
    return user_data


def get_users() -> list[User]:
    return users_db


# ---------- COURSE SERVICES ----------
def create_course(course: CourseCreate) -> Course:
    new_id = len(courses_db) + 1
    course_data = Course(id=new_id, **course.model_dump())
    courses_db.append(course_data)
    return course_data


def get_courses() -> list[Course]:
    return courses_db


# ---------- ENROLLMENT SERVICES ----------
def create_enrollment(enrollment: EnrollmentCreate) -> Enrollment:
    new_id = len(enrollments_db) + 1
    enrollment_data = Enrollment(id=new_id, **enrollment.model_dump())
    enrollments_db.append(enrollment_data)
    return enrollment_data


def get_enrollments() -> list[Enrollment]:
    return enrollments_db
