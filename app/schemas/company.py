from pydantic import BaseModel


class Company(BaseModel):
    id: int | None = None
    name: str


#Não pode ter duas companies com o mesmo nome