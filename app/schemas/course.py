from pydantic import BaseModel


class Course(BaseModel):
    id: int | None = None
    company_id: int
    name: str


#Não pode cursos com o mesmo nome da mesm company