import bcrypt
from pwinput import pwinput
from database.conexao import conectar

while True:
    usuario = input("Digite o nome do usuário: ").strip()

    if usuario:
        break

    print("O nome do usuário não pode estar vazio.")

while True:
    senha = pwinput("Digite a senha: ")

    if senha:
        break

    print("A senha não pode estar vazia.")

senha_hash = bcrypt.hashpw(
    senha.encode("utf-8"),
    bcrypt.gensalt()
)

conexao = conectar()
cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO usuarios (nome_usuario, senha_hash) VALUES (%s, %s)",
    (usuario, senha_hash.decode("utf-8"))
)
conexao.commit()
conexao.close()




























# senha = "123456"

# senha_hash = bcrypt.hashpw(
#     senha.encode("utf-8"),
#     bcrypt.gensalt()
# )

# print(senha_hash)


# senha_digitada = "12356"

# if bcrypt.checkpw(senha_digitada.encode("utf-8"), senha_hash):
#     print("Senha correta!")
# else:
#     print("Senha incorreta!")