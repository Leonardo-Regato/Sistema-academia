from database.conexao import conectar
import bcrypt

def autenticar(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT senha_hash FROM usuarios WHERE nome_usuario = %s",
        (usuario,)
    )
    resultado = cursor.fetchone()
    if resultado is None:
        conexao.close()
        return False
    else:
        senha_hash_banco = resultado[0].encode("utf-8")
        resultado = bcrypt.checkpw(
        senha.encode("utf-8"),
        senha_hash_banco
    )
    conexao.close()
    return resultado