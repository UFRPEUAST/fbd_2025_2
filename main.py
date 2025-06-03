from fastapi import FastAPI
from app.controllers.company_controller import company_router
from app.controllers.course_controller import course_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(company_router)
app.include_router(course_router)
