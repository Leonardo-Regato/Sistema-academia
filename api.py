from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from services.autenticacao import autenticar
from services.tokens import criar_token, verificar_token
from services.academia import Academia
from schemas.aluno import AlunoResponse, AlunoCreate, AlunoNomeUpdate, AlunoDataUpdate
from schemas.professor import ProfessorCreate, ProfessorDataUpdate, ProfessorNomeUpdate, ProfessorResponse
from database.conexao import conectar

app = FastAPI()
academia = Academia()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario_valido = autenticar(
        form_data.username,
        form_data.password
    )

    if not usuario_valido:
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha inválidos",
            headers={"WWW-Authenticate": "Bearer"}
        )

    token = criar_token(form_data.username)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def obter_usuario_atual(token: str = Depends(oauth2_scheme)):
    usuario = verificar_token(token)

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id FROM usuarios WHERE nome_usuario = %s",
        (usuario,)
    )
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    if resultado is None:
        raise HTTPException(
            status_code=401,
            detail="Usuário não encontrado"
        )
    return usuario



@app.post("/alunos", response_model=AlunoResponse, status_code=201)
def criar_aluno(aluno: AlunoCreate, usuario: str = Depends(obter_usuario_atual)):
    try:
        return academia.cadastra_aluno(aluno.nome, aluno.data_nascimento)
    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=f"ERROR: {e}"
        )

    
@app.get("/alunos", response_model=list[AlunoResponse])
def listar_alunos(nome: str | None = None, usuario: str = Depends(obter_usuario_atual)):
    try:
        if nome:
            return academia.buscar_aluno(nome)

        return academia.listar_alunos()
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=f"ERROR: {e}"
        )



@app.patch("/alunos/{id_aluno}/nome",response_model=AlunoResponse)
def alterar_nome_aluno(id_aluno: int, dados: AlunoNomeUpdate, usuario: str = Depends(obter_usuario_atual)):
    try:
        return academia.alterar_nome_aluno(id_aluno, dados.nome)
    except ValueError as e:
        mensagem = str(e)
        status = 404 if "ID informado não foi encontrado" in mensagem else 422
        raise HTTPException(status_code=status, detail=mensagem)
    

@app.patch("/alunos/{id_aluno}/data_nascimento",response_model=AlunoResponse)
def alterar_data_aluno(id_aluno: int, dados: AlunoDataUpdate, usuario: str = Depends(obter_usuario_atual)):
    try:
        return academia.alterar_data_aluno(id_aluno, dados.data_nascimento)
    except ValueError as e:
        mensagem = str(e)
        status = 404 if "ID informado não foi encontrado" in mensagem else 422
        raise HTTPException(status_code=status, detail=mensagem)


@app.delete("/alunos/{id_aluno}")
def remover_aluno(id_aluno: int, usuario: str = Depends(obter_usuario_atual)):
    try:
        academia.remover_aluno(id_aluno)
        return {"mensagem": "Aluno removido com sucesso."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))



@app.post("/professores", response_model=ProfessorResponse, status_code=201)
def criar_professor(professor: ProfessorCreate, usuario: str = Depends(obter_usuario_atual)):
    try:
        return academia.cadastrar_professor(professor.nome, professor.data_nascimento)
    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=f"ERROR: {e}"
        )


@app.get("/professores", response_model=list[ProfessorResponse])
def listar_professores(nome: str | None = None, usuario: str = Depends(obter_usuario_atual)):
    try:
        if nome:
            return academia.buscar_professor(nome)

        return academia.listar_professores()
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=f"ERROR: {e}"
        )
    


@app.patch("/professores/{id_prof}/nome",response_model=ProfessorResponse)
def alterar_nome_professor(id_prof: int, dados: ProfessorNomeUpdate, usuario: str = Depends(obter_usuario_atual)):
    try:
        return academia.alterar_nome_professor(id_prof, dados.nome)
    except ValueError as e:
        mensagem = str(e)
        status = 404 if "ID informado não foi encontrado" in mensagem else 422
        raise HTTPException(status_code=status, detail=mensagem)
    

@app.patch("/professores/{id_prof}/data_nascimento",response_model=ProfessorResponse)
def alterar_data_professor(id_prof: int, dados: ProfessorDataUpdate, usuario: str = Depends(obter_usuario_atual)):
    try:
        return academia.alterar_data_professor(id_prof, dados.data_nascimento)
    except ValueError as e:
        mensagem = str(e)
        status = 404 if "ID informado não foi encontrado" in mensagem else 422
        raise HTTPException(status_code=status, detail=mensagem)
    

@app.delete("/professores/{id_prof}")
def remover_professor(id_prof: int, usuario: str = Depends(obter_usuario_atual)):
    try:
        academia.remover_professor(id_prof)
        return {"mensagem": "Professor removido com sucesso."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

