from fastapi import APIRouter

from app.schemas.company import Company
from app.schemas.course import Course
from app.service.course_service import CourseService

course_router = APIRouter(prefix="/course", tags=["Curso"])
service = CourseService()


@course_router.post("/", response_model=Course)
async def create_course(course: Course):
    course.id=10
    return course


@course_router.get("/")
async def get_courses(name: str | None = None) -> list[Course]:
    print('name', name)
    return service.get_courses()

@course_router.get("/{item_id}")
async def get_course_by_id(_id):
    print('_id', _id)
    return None

@course_router.get("/{company_id}")
async def get_course_by_company_id(company_id):
    print('company_id', company_id)
    return None