from pydantic import BaseModel
from datetime import date

class AlunoResponse(BaseModel):
    id: int
    nome: str
    data_nascimento: date
    idade: int


class AlunoCreate(BaseModel):
    nome: str
    data_nascimento: date

class AlunoNomeUpdate(BaseModel):
    nome: str

class AlunoDataUpdate(BaseModel):
    data_nascimento: date