from fastapi import APIRouter, HTTPException

from app.connection.database import DataBaseConnect
from app.schemas.company import Company
from app.service.company_service import CompanyService

company_router = APIRouter(prefix="/company", tags=["Empresa"])
service = CompanyService()


@company_router.post("/", response_model=Company)
async def create_company(company: Company):
    return service.create_company(company)


@company_router.get("/")
async def get_companies(name: str | None = None) -> list[Company]:
    return service.get_companies()

@company_router.get("/{item_id}")
async def get_company(item_id):
    print('item_id', item_id)
    return None

