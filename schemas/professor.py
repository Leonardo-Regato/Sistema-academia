from pydantic import BaseModel
from datetime import date

class ProfessorResponse(BaseModel):
    id: int
    nome: str
    data_nascimento: date
    idade: int


class ProfessorCreate(BaseModel):
    nome: str
    data_nascimento: date

class ProfessorNomeUpdate(BaseModel):
    nome: str

class ProfessorDataUpdate(BaseModel):
    data_nascimento: date