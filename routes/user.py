from fastapi import APIRouter, HTTPException, status
from schemas.user import UserCreate, User
from schemas.course import CourseCreate, Course
from schemas.enrollment import EnrollmentCreate, Enrollment
from services import user as user_service

router = APIRouter()

# ---------- USER ROUTES ----------
@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    return user_service.create_user(user)


@router.get("/users/", response_model=list[User])
def get_users():
    return user_service.get_users()


# ---------- COURSE ROUTES ----------
@router.post("/courses/", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate):
    return user_service.create_course(course)


@router.get("/courses/", response_model=list[Course])
def get_courses():
    return user_service.get_courses()


# ---------- ENROLLMENT ROUTES ----------
@router.post("/enrollments/", response_model=Enrollment, status_code=status.HTTP_201_CREATED)
def create_enrollment(enrollment: EnrollmentCreate):
    return user_service.create_enrollment(enrollment)


@router.get("/enrollments/", response_model=list[Enrollment])
def get_enrollments():
    return user_service.get_enrollments()
