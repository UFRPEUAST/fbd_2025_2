from fastapi import HTTPException

from app.repository.CompanyRepository import CompanyRepository
from app.schemas.company import Company


class CompanyService:

    def __init__(self):
        self.data_base = CompanyRepository()

    def get_companies(self) -> list[Company]:
        results = self.data_base.get_all()
        empresas =[]
        for result in results:
            empresas.append(Company(id=result[0]))
        return empresas

    def create_company(self, company:Company) -> Company:
        #validar se já existe uma companyu com o mesmo nome
        # se não existir, salvar.
        # company = self.data_base.get_by_name(company.name)
        # if not company:
        #     return self.data_base.create(company)
        raise HTTPException(status_code=400, detail="Já existe uma company com esse nome ")


