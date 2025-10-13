from fastapi import APIRouter, HTTPException
from schemas.enrollment import Enrollment, EnrollmentCreate
from datetime import date
from typing import List

router = APIRouter()

enrollments: List[Enrollment] = []
next_enrollment_id = 1

@router.post("/", response_model=Enrollment, status_code=201)
def create_enrollment(enrollment: EnrollmentCreate):
    global next_enrollment_id
    for e in enrollments:
        if e.user_id == enrollment.user_id and e.course_id == enrollment.course_id:
            raise HTTPException(status_code=400, detail="User already enrolled in this course")
    new_enrollment = Enrollment(
        id=next_enrollment_id,
        user_id=enrollment.user_id,
        course_id=enrollment.course_id,
        enrolled_date=str(date.today()),
        completed=False
    )
    enrollments.append(new_enrollment)
    next_enrollment_id += 1
    return new_enrollment

@router.get("/", response_model=List[Enrollment])
def get_enrollments():
    return enrollments

@router.get("/{enrollment_id}", response_model=Enrollment)
def get_enrollment(enrollment_id: int):
    for e in enrollments:
        if e.id == enrollment_id:
            return e
    raise HTTPException(status_code=404, detail="Enrollment not found")

@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int):
    for i, e in enumerate(enrollments):
        if e.id == enrollment_id:
            del enrollments[i]
            return {"message": "Enrollment deleted successfully"}
    raise HTTPException(status_code=404, detail="Enrollment not found")
