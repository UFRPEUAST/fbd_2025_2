from app.repository.CourseRepository import CourseRepository
from app.schemas.course import Course


class CourseService:

    def __init__(self):
        self.data_base = CourseRepository()

    def get_courses(self) -> list[Course]:
        result = self.data_base.get_all()
        print('aaaaa', result[0])
        return []
